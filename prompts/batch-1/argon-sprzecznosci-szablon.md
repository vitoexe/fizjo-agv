# Argon — szablon na nierozstrzygnięte sprzeczności

Rola: **drogi, tylko** gdy po krokach Deep Research → Gemini → Cursor → Claude dwa lub więcej źródeł pierwotnych nadal sobie przeczą. Jedna sprzeczność na zapytanie.

```
I need an adjudication of a specific contradiction in the sports-medicine literature, for an open-source, evidence-graded physiotherapy knowledge base for aggressive inline skaters (AGV).

CONTRADICTION
- Claim under dispute: <one sentence>
- Source A says: <claim> — <first author, year, title, DOI/link> — design: <RCT/review/observational/consensus> — population: <...>, n=<...>
- Source B says: <claim> — <first author, year, title, DOI/link> — design: <...> — population: <...>, n=<...>
- (optional) Source C: ...
- What we already checked: <which steps/tools, what was found>
- Why it matters for AGV: <e.g. decides when a skater can return to soul grinds>

TASKS
1. Read both sources (full text if possible). Explain WHY they disagree: population, dose, outcome measure, follow-up, design quality, risk of bias, conflicts of interest.
2. Search for the best higher-level evidence that resolves it (systematic reviews, newer RCTs, guidelines), with DOIs.
3. Give a graded verdict: RESOLVED in favour of A / B, CONTEXT-DEPENDENT (state contexts), or UNRESOLVED (state what study would resolve it).

RULES
RULES (mandatory):
1. Every claim must cite a primary source with a working link or DOI (prefer DOI / PubMed / PMC). No source = do not state the claim.
2. Label every claim with exactly one of: EVIDENCE:review | EVIDENCE:RCT | EVIDENCE:observational | CONSENSUS | BIOMECH-INFERENCE | ANALOGY:<sport/population> (add to another label) | SPECULATION.
3. Keep evidence strictly separate from biomechanical inference and from practitioner opinion.
4. Never invent numbers, authors, titles or DOIs. Only report a number if it appears in the cited source; say whether you saw it in the abstract or full text.
5. If no data exists, write "NO DATA FOUND" for that question instead of guessing. A clear "nothing found" is a valid result.
6. AI models (including you) are not sources. Cite what you found, not your own knowledge without a source.
7. Do not repeat the sources we already have (listed below) unless you found something that contradicts or corrects them; we especially want SECOND, INDEPENDENT sources for existing claims.

OUTPUT FORMAT (Markdown)
### Verdict
<RESOLVED-A | RESOLVED-B | CONTEXT-DEPENDENT | UNRESOLVED> — confidence: high/med/low

### Why the sources disagree
| Factor | Source A | Source B |
|---|---|---|

### Additional evidence
| Source | Label | DOI/link | What it shows |
|---|---|---|---|

### Wording for the knowledge base (Polish, 1–3 sentences, with [source] and {LABEL})
<...>

### Remaining unknowns
- ...
```
