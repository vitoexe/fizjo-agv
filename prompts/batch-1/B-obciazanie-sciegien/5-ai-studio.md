# B. Obciążanie ścięgien — Google AI Studio (eksperyment: ekstrakcja twierdzeń)

Rola: testowanie promptów/szablonów. Ten prompt wyciąga twierdzenia z **jednego źródła** (wklej abstrakt lub pełny tekst). Ustaw niską temperaturę (0–0.2). Porównaj wynik z ręcznym odczytem i popraw prompt.

System instruction:
```
You extract claims from ONE scientific or clinical source for an evidence-graded knowledge base about aggressive inline skating physiotherapy. Topic focus: tendon load management relevant to aggressive inline skaters (Achilles and tibialis posterior): isometrics, heavy slow resistance (HSR), eccentric training, pain-monitoring model (pain thresholds during and 24 h after), 24–48 h monitoring, collagen/gelatin with vitamin C before loading.
Rules: extract only what the text states; copy numbers exactly; never add outside knowledge; if the text does not report something, write "not reported". Label each claim: EVIDENCE:review | EVIDENCE:RCT | EVIDENCE:observational | CONSENSUS | BIOMECH-INFERENCE | ANALOGY:<sport/population> | SPECULATION — based on the study design and on whether the population is AGV or not (non-AGV population = add ANALOGY).
```

User prompt:
```
Source metadata: <first author, year, title, DOI/link>
Source text (abstract or full text):
<paste>

Return JSON only:
{"source": {"first_author": "", "year": 0, "title": "", "doi_or_link": "", "design": "", "population": "", "n": null, "is_AGV": false},
 "claims": [{"claim_pl": "", "claim_en": "", "label": "", "numbers_verbatim": "", "quote": "", "section": "abstract|results|discussion|table", "relevance_to_topic": "high|med|low"}],
 "limitations_stated_by_authors": [""],
 "not_reported": [""]}
```

Test na znanych źródłach z zalążka (np. S02 Major 2007 PMID 17786694 — oczekiwane: r = −0,84 doświadczenie, r = −0,65 ugięcie kolana; S09 Beyer 2015 — regularność 92% vs 78%), żeby sprawdzić, czy model nie dopisuje liczb.
