#!/usr/bin/env python3
"""Render the course's original teaching diagrams from reviewed logical specs."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site/figures/lessons'
COLORS = {'record': '#f4f1e8', 'derived': '#edf3f8', 'current': '#edf4ef', 'control': '#f4eee7'}


def wrap(text, units):
    lines, line, width = [], '', 0
    for char in text:
        size = 2 if unicodedata.east_asian_width(char) in 'WF' else 1
        if char == '\n' or (line and width + size > units):
            lines.append(line)
            line, width = '', 0
        if char != '\n':
            line += char
            width += size
    if line:
        lines.append(line)
    return lines or ['']


class Figure:
    def __init__(self, spec):
        self.spec = spec
        self.parts = []
        self.boxes = []
        self.text(28, 38, spec['title'], 24, 600)
        self.text(28, 68, spec.get('subtitle', '原创教学示意'), 16, 400, '#586b67', 82)

    def text(self, x, y, text, size=18, weight=400, color='#243735', units=76):
        lines = wrap(text, units)
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">')
        for i, line in enumerate(lines):
            self.parts.append(f'<tspan x="{x}" dy="{0 if not i else size * 1.6}">{escape(line)}</tspan>')
        self.parts.append('</text>')
        return y + (len(lines) - 1) * size * 1.6

    def line(self, x1, y1, x2, y2, arrow=False, control=False):
        self.parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="#798b85" stroke-width="1.6" fill="none"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="5 4"' if control else '')+'/>')

    def node_height(self, node, width):
        units = int((width - 36) / 9)
        title_lines = len(wrap(node['title'], int((width - 36) / 10)))
        body_lines = sum(len(wrap(t, units)) for t in node.get('lines', []))
        return int(24 + title_lines * 32 + body_lines * 29 + 16)

    def node(self, node, x, y, width, height=None):
        height = height or self.node_height(node, width)
        fill = COLORS.get(node.get('kind'), '#ffffff')
        self.parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="3" fill="{fill}" stroke="#c8d1ca"/>')
        bottom = self.text(x+18, y+32, node['title'], 20, 600, units=int((width-36)/10))
        for line in node.get('lines', []):
            bottom = self.text(x+18, bottom+29, line, 18, units=int((width-36)/9))
        self.boxes.append((x, y, width, height))
        return y + height

    def split_connection(self, source, target, control=False):
        ax, ay, aw, ah = self.boxes[source]
        bx, by, bw, bh = self.boxes[target]
        if ay == by:
            if ax < bx:
                self.line(ax + aw + 3, ay + 32, bx - 3, by + 32, True, control)
            else:
                self.line(ax - 3, ay + 32, bx + bw + 3, by + 32, True, control)
            return

        # A shared, full-width input or result retains a separate vertical
        # connection for each column. Do not merge independent evidence paths.
        if ax == bx or aw == 680 or bw == 680:
            x = bx + bw / 2 if aw > bw else ax + aw / 2
            start, end = (ay + ah + 3, by - 3) if by > ay else (ay - 3, by + bh + 3)
            intervening = any(
                i not in (source, target) and rx < x < rx + rw
                and min(start, end) < ry + rh and max(start, end) > ry
                for i, (rx, ry, rw, rh) in enumerate(self.boxes)
            )
            if not intervening:
                self.line(x, start, x, end, True, control)
                return

        # Cross-column routes stay in the gutter; longer same-column routes
        # go outside the boxes. Opposing paths use different rails.
        if ax != bx and aw == bw:
            rail = 364 if ax < bx else 372
            start_x = ax + aw + 2 if ax < bx else ax - 2
            end_x = bx - 2 if ax < bx else bx + bw + 2
        else:
            rail = 12 if ax == 28 else 724
            start_x = ax if rail < ax else ax + aw
            end_x = bx - 2 if rail < bx else bx + bw + 2
        self.parts.append(
            f'<path d="M{start_x},{ay + ah / 2} H{rail} V{by + bh / 2} H{end_x}" '
            'stroke="#798b85" stroke-width="1.6" fill="none" marker-end="url(#arrow)"'
            + (' stroke-dasharray="5 4"' if control else '') + '/>'
        )

    def render(self):
        spec, y = self.spec, 106
        nodes = spec['nodes']
        if spec['layout'] == 'split':
            i = 0
            while i < len(nodes):
                if nodes[i].get('span') == 2:
                    y = self.node(nodes[i], 28, y, 680) + 24
                    i += 1
                    continue
                row = nodes[i:i+2]
                if len(row) == 2 and row[1].get('span') == 2:
                    row = row[:1]
                height = max(self.node_height(n, 330) for n in row)
                for k, n in enumerate(row):
                    self.node(n, 28+k*350, y, 330, height)
                y += height + 24
                i += len(row)
        elif spec['layout'] == 'hierarchy':
            depths = []
            for i, n in enumerate(nodes):
                parent = n.get('parent')
                if parent is not None and (type(parent) is not int or parent < 0 or parent >= i):
                    raise ValueError(f'Invalid parent in {spec["id"]}')
                depth = 0 if parent is None else depths[parent]+1
                depths.append(depth)
                x = 28+depth*44
                if parent is not None:
                    px, py, pw, ph = self.boxes[parent]
                    self.line(x-22, py+ph, x-22, y+24)
                    self.line(x-22, y+24, x, y+24)
                y = self.node(n, x, y, 680-depth*44)+20
        else:
            for i, n in enumerate(nodes):
                if spec['layout'] == 'timeline':
                    self.parts.append(f'<circle cx="42" cy="{y+25}" r="6" fill="#235f55"/>')
                    if i:
                        px, py, pw, ph = self.boxes[-1]
                        self.line(42, py+25, 42, y+19)
                    y = self.node(n, 68, y, 640)+24
                else:
                    y = self.node(n, 28, y, 680)+20
                edge = next((e for e in spec.get('connections', []) if e['from']==i and e['to']==i+1), None)
                if edge:
                    self.line(368, y-14, 368, y+26, True, edge.get('kind') == 'control')
                    self.text(390, y+10, edge.get('label',''), 16, color='#586b67', units=35)
                    y += 40
        # Keep precise relationship labels below the nodes as well as visible edges.
        extra = [e for e in spec.get('connections', []) if spec['layout'] in ('split','hierarchy') or e['to']!=e['from']+1]
        flow_origins = list(dict.fromkeys(e['from'] for e in extra))
        for e in extra:
            a,b=e['from'],e['to']
            if not (0<=a<len(nodes) and 0<=b<len(nodes)):
                raise ValueError(f'Invalid edge in {spec["id"]}')
            ax, ay, aw, ah = self.boxes[a]
            bx, by, bw, bh = self.boxes[b]
            if spec['layout'] == 'split':
                self.split_connection(a, b, e.get('kind') == 'control')
            elif spec['layout'] == 'flow':
                # Branches need a visible route as well as their precise caption.
                # Keep the line outside the content boxes, with the target arrow
                # pointing back into the target's left edge.
                rail = (12 if len(flow_origins) == 1 else
                        6 + 16 * flow_origins.index(a) / (len(flow_origins) - 1))
                self.parts.append(
                    f'<path d="M{ax},{ay + ah / 2} H{rail} V{by + bh / 2} H{bx - 2}" '
                    'stroke="#365e7c" stroke-width="1.6" fill="none" marker-end="url(#arrow)"'
                    + (' stroke-dasharray="5 4"' if e.get('kind') == 'control' else '') + '/>'
                )
            relation=f'{nodes[a]["title"]} → {nodes[b]["title"]}：{e.get("label", "")}'
            y=self.text(28,y+12,relation,16,color='#365e7c',units=82)+26
        y=self.text(28,y+12,spec.get('footer',''),16,color='#586b67',units=82)+30
        height=int(y)
        head=[f'<svg xmlns="http://www.w3.org/2000/svg" width="736" height="{height}" viewBox="0 0 736 {height}" role="img" aria-labelledby="title desc">',
              f'<title id="title">{escape(spec["title"])}</title><desc id="desc">{escape(spec["alt"])}</desc>',
              '<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#798b85"/></marker></defs>',
              f'<rect width="736" height="{height}" fill="#fdfcf9"/>',
              '<g font-family="PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif">']
        return '\n'.join(head+self.parts+['</g></svg>']),height


def build(specs):
    result = {}
    for spec in specs:
        if not re.fullmatch(r'[a-z0-9-]+',spec['id']):
            raise ValueError('Invalid figure identifier')
        if spec['layout'] not in {'flow','split','hierarchy','timeline'}:
            raise ValueError('Unknown figure layout')
        if not spec.get('nodes'):
            raise ValueError('Empty figure')
        for edge in spec.get('connections', []):
            if any(type(edge.get(k)) is not int or not 0 <= edge[k] < len(spec['nodes'])
                   for k in ('from', 'to')):
                raise ValueError(f'Invalid edge in {spec["id"]}')
        svg,height=Figure(spec).render()
        result[spec['id']] = {'svg': svg, 'height': height}
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    specs=json.loads((OUT/'specs.json').read_text())
    rendered=build(specs)
    for name,data in rendered.items():
        file=OUT/(name+'.svg')
        if args.check:
            if not file.exists() or file.read_text()!=data['svg']:
                raise SystemExit(f'Outdated diagram: {file}')
        else:file.write_text(data['svg'])
    print(f'{len(rendered)} lesson diagrams '+('checked' if args.check else 'generated'))


if __name__=='__main__':
    main()
