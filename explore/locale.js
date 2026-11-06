/* Shared rendering messages. IDs, relationships and source URLs stay language-neutral. */
(function (root) {
  'use strict';
  const ui = {
    systems: 'System', papers: 'Paper', benchmarks: 'Evaluation', fiction: 'Literature & screen',
    documented: 'Documented example', synthesis: 'Editorial connection',
    conceptTag: 'Concept / reading lens',
    outside: 'Selection retained · outside this perspective’s focus',
    distinction: 'Keep the distinction', connections: 'Connected concepts',
    why: '{kind} · why this connection', reference: 'Read cited reference ↗',
    representatives: 'Representative resources', representativeIntro: 'Starting points, not an exhaustive capability list.',
    literary: 'Literary connections · {count}', literaryIntro: 'Editorial analogies to help ask questions. These are not technical evidence.',
    perspective: 'Perspective {number} / 03', announcement: '{view} perspective. Selected: {concept}',
    back: '← Back to the library', compare: 'How to compare reported results', analogy: 'Editorial analogy',
    entry: 'Read {kind} entry ↗', sources: 'Go to the source',
    analogyNote: 'The literary connection is an editorial interpretation, not a scientific or engineering result.',
    resourceNote: 'A source-backed reading entry. Inclusion does not imply installation, independent benchmark reproduction, or a security audit.',
    library: 'The complete reading library', libraryTitle: '{count} resources, many perspectives',
    libraryIntro: 'The map highlights representative connections. Other entries remain available here; an unmapped resource is not an unsupported resource.',
    technical: 'Technical examples · {count}', stories: 'Literary analogies · {count}', more: 'More resources · {count}',
    curated: '{count} curated resources', coverage: '{concepts} concepts · {technical} technical examples · {stories} literary analogies',
    checked: 'Sources checked · {date}'
  };

  function localize(content, resources, translation) {
    if (!translation) return { content, resources };
    return {
      content: {
        ...content,
        views: content.views.map(item => ({ ...item, ...translation.views[item.id] })),
        concepts: content.concepts.map(item => ({ ...item, ...translation.concepts[item.id] })),
        edges: content.edges.map(item => ({ ...item, ...translation.edges[item.id] }))
      },
      resources: resources.map(item => ({
        ...item,
        ...translation.resources[item.id],
        ...(item.evaluationNote ? { evaluationNote: translation.evaluationNote } : {}),
        sources: item.sources.map(source => ({ ...source, label: translation.sourceLabels[source.label] }))
      }))
    };
  }

  const api = { ui, localize };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.AtlasLocale = api;
})(globalThis);
