# G. Prewencja i periodyzacja obciążenia sesji — Google AI Studio (eksperyment: ekstrakcja twierdzeń)

Rola: testowanie promptów/szablonów. Ten prompt wyciąga twierdzenia z **jednego źródła** (wklej abstrakt lub pełny tekst). Ustaw niską temperaturę (0–0.2). Porównaj wynik z ręcznym odczytem i popraw prompt.

System instruction:
```
You extract claims from ONE scientific, clinical or coaching source for an evidence-graded knowledge base about preparing the body for aggressive inline skating grinds. Topic focus: injury prevention and session load periodisation for aggressive inline skaters: warm-up content and duration, number of high-impact landings/drops per session, session frequency and rest days, fatigue and late-session injury risk, progression of trick difficulty, protective equipment (wrist guards, knee pads, helmets), concussion protocols, load-monitoring tools usable by amateur skaters.
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

Test na znanym źródle z zalążka: S04 Schieber 1996 PMID 8929359 — oczekiwane: OR 10,4 dla urazu nadgarstka bez ochraniaczy — sprawdź, czy model nie dopisuje liczb.
