#!/usr/bin/env python3
"""Generate the teaching diagrams for the three illustrated sample chapters."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site/figures/pilot'
INK, MUTED, RULE = '#243735', '#586b67', '#cdd5cf'
TEAL, BLUE, OCHRE = '#235f55', '#365e7c', '#8a5d28'


class Diagram:
    def __init__(self, height, title, desc):
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="736" height="{height}" viewBox="0 0 736 {height}" role="img" aria-labelledby="title desc">',
                      f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
                      '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#586b67"/></marker></defs>',
                      f'<rect width="736" height="{height}" fill="#fdfcf9"/>',
                      '<g font-family="PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif">']
        self.text(24, 35, title, 24, INK, 600)
        self.text(24, 64, '教学示意 · 人物、日期与结果为假设', 16, MUTED)

    def text(self, x, y, value, size=18, color=INK, weight=400, leading=None):
        leading = leading or size * 1.55
        lines = value.split('\n')
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">')
        for i, line in enumerate(lines):
            self.parts.append(f'<tspan x="{x}" dy="{0 if i == 0 else leading}">{escape(line)}</tspan>')
        self.parts.append('</text>')

    def box(self, x, y, w, h, fill='#ffffff', stroke=RULE, dash=None):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="1.3"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')

    def line(self, x1, y1, x2, y2, color=MUTED, arrow=False, width=2, dash=None):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')

    def path(self, value, arrow=True, dash=None):
        self.parts.append(f'<path d="{value}" fill="none" stroke="{MUTED}" stroke-width="1.8"'+(' marker-end="url(#arrow)"' if arrow else '')+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')

    def save(self, name):
        (OUT / name).write_text('\n'.join(self.parts + ['</g></svg>']))


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    d = Diagram(520, 'A1  一张笔记，几种不同来源的字段', '原始内容与交互时间；模型生成关键词标签上下文；由文本计算向量；链接记录关联。')
    for x, fill, heading in [(24,'#fff','原始记录'),(266,'#edf4ef','模型补充的解释'),(508,'#eff3f7','查找用的表示')]:
        d.box(x,100,204,256,fill)
        d.text(x+14,132,heading,20,INK,600)
    d.text(38,173,'原文节选\n“打算每天练半小时”\n\n交互时间\n3 月 1 日',17)
    d.text(280,173,'关键词：吉他、练习\n标签：兴趣、安排\n\n上下文描述：\n开始建立练琴习惯',17)
    d.text(522,173,'向量 embedding\n\n原文＋关键词＋\n标签＋上下文\n编码成一串数字',17)
    d.line(230,219,260,219,arrow=True)
    d.line(472,219,502,219,arrow=True)
    d.text(280,338,'生成内容需要核对',16,TEAL)
    d.box(24,386,688,104,'#f5f2e9')
    d.text(40,416,'还有一个字段：链接',19,INK,600)
    d.text(40,449,'当前笔记',18)
    d.line(142,443,278,443,arrow=True)
    d.text(290,449,'另一条相关笔记',18)
    d.text(40,477,'写入时判断关联；没有建立关联时，链接集合为空。',16,MUTED)
    d.save('amem-note.svg')

    d = Diagram(740, 'A2  新记录怎样影响旧笔记', '先有每天练琴的N1；N2记录隔天练的决定；模型判断关联后可能更新N1的解释字段，原文及时间不改。')
    d.box(24,91,688,136)
    d.text(42,122,'01  已有 N1',20,INK,600)
    d.text(42,157,'原文：“打算每天练半小时。”    时间：3 月 1 日',18)
    d.text(42,191,'上下文：“开始建立练琴习惯”',18)
    d.line(368,230,368,259,arrow=True)
    d.box(24,269,688,157,'#eff3f7')
    d.text(42,301,'02  写入 N2，找到候选 N1',20,INK,600)
    d.text(42,337,'3 月 5 日：“这几天手指疼，我决定改成隔天练。”',18)
    d.text(42,374,'假设模型判断两条记录有关，建立 N2 → N1 的链接。',18,BLUE)
    d.text(42,407,'这里记录小林的决定，不做原因诊断。',16,MUTED)
    d.line(368,430,368,459,arrow=True)
    d.box(24,469,688,218,'#edf4ef')
    d.text(42,501,'03  N1 的说明可能更新；N2 也留在集合里',20,INK,600)
    d.text(42,539,'N1 原文与时间：仍保留最初的计划及其日期。',18)
    d.box(40,561,650,103,'#fff',TEAL,'5 4')
    d.text(54,591,'更新的部分：上下文、关键词、标签',18,TEAL,600)
    d.text(54,623,'上下文示例：“练琴习惯；近期有练习调整记录”',18)
    d.text(54,648,'虚线框只标出可演化的说明，不表示额外历史副本。',16,MUTED)
    d.text(24,717,'写入会改变记忆的组织方式；是否发生、是否正确，需要检查结果。',16,MUTED)
    d.save('amem-evolution.svg')

    d = Diagram(540, 'G1  从一条消息，到有出处的关系', '消息E2保存在图中，抽取为小林和杭州实体及居住关系；关系追溯到E2。')
    d.box(24,94,652,111)
    d.text(42,126,'原始消息 E2',20,INK,600)
    d.text(42,162,'“我 5 月 1 日已经搬到杭州住了。”',20)
    d.text(42,188,'5 月 3 日送入系统；保留原文供之后核对。',16,MUTED)
    d.line(350,208,350,270,arrow=True)
    d.text(372,246,'抽取实体与关系',17,MUTED)
    d.box(76,284,168,70,'#edf4ef',TEAL)
    d.box(450,284,168,70,'#edf4ef',TEAL)
    d.text(124,327,'小林',24,TEAL,600)
    d.text(500,327,'杭州',24,TEAL,600)
    d.line(246,319,444,319,arrow=True)
    d.text(310,304,'居住于',19,INK,600)
    d.box(76,387,542,94,'#eff3f7',BLUE)
    d.text(94,418,'关系事实：小林从 5 月 1 日起住杭州',18)
    d.text(94,452,'来源列表中包含 E2',18,BLUE)
    d.path('M 620 433 H 699 V 151 H 679',True,'5 4')
    d.text(620,376,'来源',16,BLUE)
    d.text(24,514,'实体与边是抽取结果；原始消息帮助核对结果是否忠实。',16,MUTED)
    d.save('graphiti-structure.svg')

    d = Diagram(620, 'G2  发生时间，与系统获知时间', '现实在5月1日搬家，系统5月3日才写入；旧关系的invalid_at和expired_at分别表示不同时间。')
    for x,label in [(260,'5/1'),(426,'5/2'),(616,'5/3')]:
        d.line(x,105,x,369,RULE,False,1,'3 5')
        d.text(x-16,96,label,17,MUTED)
    d.text(24,129,'事实时间',19,INK,600)
    d.line(96,178,257,178,OCHRE,False,5)
    d.line(261,178,700,178,TEAL,False,5)
    d.text(120,162,'住上海',18,OCHRE)
    d.text(431,162,'住杭州',18,TEAL)
    d.text(274,211,'搬家已发生',17,TEAL)
    d.text(24,271,'系统记录时间',19,INK,600)
    d.line(96,314,614,314,OCHRE,False,5)
    d.line(618,343,700,343,TEAL,False,5)
    d.text(132,300,'旧上海记录还未被标记失效',18,OCHRE)
    d.text(408,363,'5/3：处理搬家消息',17,TEAL)
    d.box(24,395,334,171,'#f5f2e9')
    d.box(378,395,334,171,'#edf4ef')
    d.text(40,426,'旧的上海关系',20,OCHRE,600)
    d.text(40,461,'事实结束：5/1',18)
    d.text(40,484,'invalid_at',16,MUTED)
    d.text(40,521,'系统标失效：5/3',18)
    d.text(40,544,'expired_at',16,MUTED)
    d.text(394,426,'新的杭州关系',20,TEAL,600)
    d.text(394,461,'事实开始：5/1',18)
    d.text(394,484,'valid_at',16,MUTED)
    d.text(394,521,'关系创建：5/3',18)
    d.text(394,544,'created_at',16,MUTED)
    d.text(24,596,'本例前提：5/3 识别出两条关系相互替代，并完成写入与更新。',16,MUTED)
    d.save('graphiti-time.svg')

    d = Diagram(620, 'L1  找到一条，与找齐全部', '两次旅行总花费需证据会话A和B。前五条结果只命中A，因此any为1，all为0。')
    d.text(24,104,'问题：两次旅行总花费？   所需证据：A（600元）和 B（900元）',17)
    rows=[('1','其他会话','没有本题所需金额'),('2','会话 A · 苏州 600 元','证据 · 命中'),('3','其他会话','没有本题所需金额'),('4','其他会话','没有本题所需金额'),('5','其他会话','没有本题所需金额')]
    for i,(rank,title,note) in enumerate(rows):
        y=128+i*48
        d.box(24,y,688,43,'#edf4ef' if rank=='2' else '#fff',TEAL if rank=='2' else RULE)
        d.text(42,y+29,rank,18,MUTED)
        d.text(92,y+29,title,18,TEAL if rank=='2' else INK,600 if rank=='2' else 400)
        d.text(458,y+29,note,16,MUTED)
    d.box(24,391,688,65,'#f5f2e9')
    d.text(42,419,'会话 B · 杭州 900 元',19,OCHRE,600)
    d.text(42,444,'也是必需证据，但没有进入这次前 5 条。',16,MUTED)
    d.box(24,482,334,88,'#edf4ef')
    d.box(378,482,334,88,'#f5f2e9')
    d.text(40,513,'至少找到一条？ 是',19,TEAL,600)
    d.text(40,547,'recall_any@5 = 1',20,TEAL)
    d.text(394,513,'所需证据取齐？ 否',19,OCHRE,600)
    d.text(394,547,'recall_all@5 = 0',20,OCHRE)
    d.text(24,600,'这是单题的手算示例，按会话计数；不是任何系统的实测成绩。',16,MUTED)
    d.save('longmemeval-retrieval.svg')

    d = Diagram(660, 'L2  系统作答与评测，分别看什么', '历史问题日期进入受测系统，检索结果交给证据评测，系统回答交给答案评测；金标准留在评测端。')
    d.text(24,102,'系统可见的输入',20,INK,600)
    d.text(267,102,'受测系统',20,INK,600)
    d.text(508,102,'仅评测端持有',20,BLUE,600)
    d.line(491,112,491,637,RULE,False,1.5,'5 5')
    d.box(24,124,212,440)
    d.text(40,157,'历史会话与日期',18,INK,600)
    d.text(40,193,'A：苏州 600 元\nB：杭州 900 元\n其他历史……',17)
    d.line(40,292,220,292,RULE,False,1)
    d.text(40,324,'问题 q',18,INK,600)
    d.text(40,358,'两次旅行\n一共花了多少？',18)
    d.text(40,451,'提问时间 tq',18,INK,600)
    d.text(40,484,'6 月 20 日',18)
    d.box(262,161,212,102,'#edf4ef')
    d.text(280,193,'检索历史',20,TEAL,600)
    d.text(280,229,'输出前 k 条结果',17)
    d.line(238,211,256,211,arrow=True)
    d.line(368,267,368,303,arrow=True)
    d.box(262,312,212,98,'#edf4ef')
    d.text(280,344,'组织本次输入',19,TEAL,600)
    d.text(280,380,'把取回内容给模型',17)
    d.line(368,414,368,463,arrow=True)
    d.box(262,473,212,90,'#edf4ef')
    d.text(280,504,'生成回答',20,TEAL,600)
    d.text(280,539,'例如：“1500 元”',17)
    d.box(508,124,204,108,'#eff3f7')
    d.text(524,156,'证据标签',19,BLUE,600)
    d.text(524,191,'本题需要 A 与 B',17)
    d.line(610,235,610,267,arrow=True)
    d.box(508,276,204,101,'#eff3f7')
    d.text(524,307,'检查检索结果',19,BLUE,600)
    d.text(524,339,'至少命中？\n是否取齐？',17)
    d.path('M 477 214 H 484 V 324 H 505')
    d.box(508,408,204,72,'#eff3f7')
    d.text(524,437,'参考答案 a',18,BLUE,600)
    d.text(524,464,'1500 元',18)
    d.line(610,483,610,516,arrow=True)
    d.box(508,526,204,105,'#eff3f7')
    d.text(524,556,'评分员按规则判分',17,BLUE,600)
    d.text(524,588,'对照问题、答案\n和系统回答',17)
    d.path('M 477 520 H 484 V 579 H 505')
    d.text(24,614,'参考答案与证据标签留在评测端。',17,MUTED)
    d.text(24,641,'它们不用于提示受测系统该去哪里找。',17,MUTED)
    d.save('longmemeval-evaluation.svg')


if __name__ == '__main__':
    build()
    print('Generated six teaching diagrams.')
