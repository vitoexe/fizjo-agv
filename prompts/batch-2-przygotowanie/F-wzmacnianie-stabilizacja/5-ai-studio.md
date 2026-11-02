# F. Program wzmacniania i stabilizacji dla AGV — Google AI Studio (eksperyment: ekstrakcja twierdzeń)

Rola: testowanie promptów/szablonów. Ten prompt wyciąga twierdzenia z **jednego źródła** (wklej abstrakt lub pełny tekst). Ustaw niską temperaturę (0–0.2). Porównaj wynik z ręcznym odczytem i popraw prompt.

System instruction:
```
You extract claims from ONE scientific, clinical or coaching source for an evidence-graded knowledge base about preparing the body for aggressive inline skating grinds. Topic focus: a strength, stability, proprioception and mobility programme to prepare the body for aggressive inline skating grinds and landings: ankle (inversion/eversion), calf (soleus/gastrocnemius), tibialis posterior, peroneals, hip (abductors, external rotators, glutes), core/trunk, wrist/forearm (fall tolerance); dosing, progression, frequency, and evidence for injury prevention.
Rules: extract only what the text states; copy numbers exactly; never add outside knowledge; if the text does not report something, write "not reported". Label each claim: EVIDENCE:review | EVIDENCE:RCT | EVIDENCE:observational | CONSENSUS | BIOMECH-INFERENCE | ANALOGY:<sport/population> | SPECULATION | OPINION — based on the study design and on whether the population is AGV or not (non-AGV population = add ANALOGY). Coaching/technique advice without data = OPINION.
```

User prompt:
```
Source metadata: <first author, year, title, DOI/link>
Source text (abstract or full text):
<paste>

Return JSON only:
{"source": {"first_author": "", "year": 0, "title": "", "doi_or_link": "", "design": "", "population": "", "sport": "", "n": null, "is_AGV": false},
 "claims": [{"claim_pl": "", "claim_en": "", "label": "", "body_region": "ankle|knee|hip|trunk|wrist|whole-body", "numbers_verbatim": "", "quote": "", "section": "abstract|results|discussion|table", "relevance_to_topic": "high|med|low"}],
 "limitations_stated_by_authors": [""],
 "not_reported": [""]}
```

Test na znanym źródle z zalążka: S09 Beyer 2015 PMID 26018970 — oczekiwane: regularność 92% (HSR) vs 78% (ekscentryka), oceny po 12 i 52 tyg. — sprawdź, czy model nie dopisuje liczb.
