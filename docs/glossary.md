+++
title = "Privacy terms, explained."
nav_label = "Glossary"
kicker = "For researchers & study participants"
description = "What privacy words mean in brain imaging, and why their meaning changes between legal frameworks."
updated = "13 November 2026"
+++
## Start here

**“Anonymous”, “de-identified” and “coded” are not interchangeable.** A label alone does not tell you whether someone can be identified, who can access the data, or which law applies. This glossary adapts the working consensus manuscript for readers without legal training. The jurisdiction tables distinguish legislation from regulatory guidance; they do not establish equivalent legal tests. [1–8](#sources)

**For participants:** ask your study team what the term means for your data, who could reconnect them to you, and what information will be shared. **For researchers:** record the framework, recipient, available additional information and assessment date alongside the term.

## Anonymisation {#anonymisation}

Processing data so that the people concerned are no longer identifiable under the applicable standard. Whether that standard is met depends on context and realistic identification methods, rather than simply removing names. Successful anonymisation is an assessed outcome, not the name of one software operation. [2–7](#sources)

### How anonymisation differs across frameworks

| Framework | Meaning or threshold | What to take away |
| --- | --- | --- |
| EU — GDPR | Identifiability is assessed using means reasonably likely to be used, from the relevant entities' perspectives. Anonymous information falls outside the GDPR's scope. [2] | Explain whose perspective and which additional information were assessed. |
| UK — UK GDPR / ICO | Anonymity depends on a contextual assessment of reasonably likely identification, including singling out and linkability. [3] | Distinct rows alone do not settle whether people are identifiable. |
| US — HIPAA | The corresponding term is **de-identification**, using Safe Harbor or Expert Determination under §164.514. Qualifying information is no longer protected health information under HIPAA. [4] | This is a particular US health-information test; it does not automatically satisfy GDPR anonymity. |
| Australia — Privacy Act / OAIC | **De-identification** requires people no longer to be identifiable or reasonably identifiable, considering the data and access environment. [5] | Removing direct identifiers alone is insufficient. |
| Québec — privacy legislation and 2024 regulation | Anonymisation requires an irreversible outcome under the statutory standard, with prescribed methods, risk analysis and reassessment. [6, 8] | Québec's requirements should not be presented as one Canada-wide rule. |
| Singapore — PDPC guidance | Anonymisation combines techniques and safeguards through a risk-based process. [7] | De-identification is only an initial step, not an equivalent outcome. |

## De-identification {#de-identification}

An umbrella expression for reducing identifiability, often by removing or changing identifiers and applying safeguards. **Its legal meaning is not uniform.** In a participant information sheet, “de-identified” needs an explanation of what was done and what identification remains possible. [1, 3–8](#sources)

| Framework | What “de-identified” means here | Does the label settle legal status? |
| --- | --- | --- |
| US — HIPAA | Safe Harbor removes specified identifiers and requires no actual knowledge of remaining identifiability; Expert Determination requires a qualified expert's assessment of very small identification risk. [4] | Meeting the applicable method removes HIPAA PHI status; names-only removal does not. |
| Australia — Privacy Act | An outcome in which individuals are no longer identifiable or reasonably identifiable. [5] | Appropriately de-identified information is outside that Act's personal-information category, subject to context. |
| EU — GDPR | Not a defined GDPR category; the distinctions include personal data, pseudonymisation and anonymous information. [2] | No. An identifiability assessment is still needed. |
| UK — DPA 2018 / ICO | Section 171 uses a specific meaning for unlawful re-identification: attribution requires additional information. [3] | No. Data described this way can remain personal data. |
| Canada — federal administrative guidance | A process reducing identifiability while recognising residual risk, distinguished from anonymisation. [8] | No automatic exclusion from the federal Privacy Act; this is not a definition for all Canadian regimes. |
| Québec — provincial legislation | Information no longer permits direct identification; this is distinct from anonymised information. [8] | No. Do not treat removal of direct identifiers as anonymisation. |
| Singapore — PDPC guidance | Removal of direct identifiers, potentially including replacement with codes. [7] | No. Other information may still enable identification. |

## Pseudonymisation and coded data {#pseudonymisation}

Replacing a name with a study code is a familiar example. Under GDPR Article 4(5), attribution requires additional information kept separately and protected. The key holder's ability to identify someone matters, as does the position of other recipients: anonymity must be assessed for the relevant context, not inferred from the code alone. [2](#sources)

**Participant example:** a scan labelled `sub-017` may still be connected to your name by an authorised study team holding a separate key. Ask who holds it and under what conditions it can be used.

## Identifiability and personal data {#identifiability}

**Identifiability** concerns whether a person can be identified directly or indirectly in the relevant context. A name is not always required. **Personal data / personal information** concerns information relating to an identified or identifiable person, with the applicable framework determining the precise scope. [2–8](#sources)

**Special categories / sensitive information:** health information can attract additional protection. GDPR “special categories” is a particular legal category; sensitive-information categories differ elsewhere. Information may be sensitive even when it contributes little to finding out who someone is. [1, 2](#sources)

## Record isolation, singling out and linkage {#singling-out}

An unusual combination can distinguish one record within a dataset. That is **record isolation**. Linking that record to a particular person in a realistic setting is a further question. **Linkage** connects records concerning the same person, potentially increasing what can be learned. [1–5](#sources)

**Illustrative example:** one row is the only record with a particular age range and occupation. This shows dataset uniqueness. Whether a neighbour, another researcher or a data recipient could connect it to someone depends on what else they know or can obtain.

### Related words are not identical legal tests

| Framework | Vocabulary | Relationship to uniqueness |
| --- | --- | --- |
| EU — EDPB Guidelines 02/2026, v1.0 | Record isolation; singling out | Isolation is a unique record; whether it singles out the person requires contextual assessment. These guidance terms are not separate Article 4 definitions. [2] |
| UK — ICO | Singling out; linkability | Differentiating rows alone is insufficient. Consider additional information and the ability to act specifically on someone, including without their name. [3] |
| US — HHS / HIPAA | Distinguishability; uniqueness; linkage | Expert assessment considers accessible identified sources and feasible matching; the EDPB's named pair is not the HIPAA test. [4] |
| Australia — OAIC | Rare characteristics; reasonable identifiability | Uniqueness contributes to a contextual assessment of practical identification, rather than forming a separately named pair of tests. [5] |
| Québec — 2024 regulation | Individualization; correlation; inference | These are defined regulatory criteria, followed by a broader re-identification risk analysis. They are not an exact translation of the EDPB distinction. [6] |
| Canada — federal terminology guidance | Individualization; “singling out” as an alternative designation | This vocabulary can describe isolation within a dataset; do not assume equivalence with the EDPB's more specific distinction. [8] |

The manuscript's **technical “singling-out” ratings** assess individual specificity and potential matching, including across sessions. They are not findings that each person is legally identifiable. [1](#sources)

## Brain fingerprinting {#brain-fingerprinting}

A research expression for individual-specific brain patterns, often tested by matching recordings across sessions or datasets. It does not itself demonstrate that a previously unknown person's real-world identity can be recovered. That would require a usable connection to an identity or other relevant context. Avoid assuming either that all such patterns identify people or that identity-linked reference data can never exist. [1](#sources)

## Re-identification and inference {#re-identification}

**Re-identification** connects data whose identifiers were removed, replaced or obscured back to a person. **Inference / attribute disclosure** concerns learning something about them, such as a diagnosis. These differ: knowing someone joined a study in which everyone has the same diagnosis may disclose that diagnosis without finding their exact record. [1, 5](#sources)

## Use the terms in practice

- **Participants:** “When you say my data are de-identified, can anyone still reconnect them to me? What can other recipients see?”
- **Researchers:** distinguish matching performance, the availability of identity-linked reference data and the legal test. Assess images and metadata together.
- **Legal and governance teams:** use the technical distinctions alongside the applicable jurisdiction, recipient perspective, safeguards and current primary sources.

Continue with [research guidance](researchers.html), [participant questions](participants.html#questions-to-ask-your-study-team) or [technical evidence for legal assessment](legal.html).

## Sources {#sources}

Bracketed numbers in the tables refer to these sources. Adapted from the manuscript's glossary and checked against the following primary guidance on **13 November 2026**. This is an explanatory draft, not a determination about a particular dataset.

1. Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*, unpublished working manuscript and glossary consulted 13 November 2026. [Associated analysis](https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io/tree/main/papers/expert-ratings).
2. EDPB, [Guidelines 02/2026 on Anonymisation, v1.0](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf). Adopted for consultation 7 July 2026; the [official listing](https://www.edpb.europa.eu/documents/guideline/guidelines-022026-on-anonymisation_en) marks consultation closed. This page does not assume a final post-consultation version.
3. ICO, [How do we ensure anonymisation is effective?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/how-do-we-ensure-anonymisation-is-effective/) and [DPA 2018, section 171](https://www.legislation.gov.uk/ukpga/2018/12/section/171).
4. HHS, [HIPAA de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html), including §164.514 and Expert Determination / Safe Harbor.
5. OAIC, [De-identification and the Privacy Act](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/handling-personal-information/de-identification-and-the-privacy-act).
6. Québec, [Regulation respecting the anonymization of personal information (2024)](https://www.publicationsduquebec.gouv.qc.ca/fileadmin/gazette/pdf_encrypte/lois_reglements/2024A/106829.pdf).
7. PDPC, [Guide to Basic Anonymisation (2024)](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/guide-to-basic-anonymisation-%28updated-24-july-2024%29.pdf). Its practical techniques concern structured textual data, not a method for anonymising brain images.
8. Canada, [Privacy Implementation Notice 2023-01, updated 2025](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/2023-01-de-identification.html); [Personal Information and Privacy Glossary](https://www.btb.termiumplus.gc.ca/publications/renseignements-personnels-personal-information-eng.html); OPC, [cross-jurisdiction comparison (2024)](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2024/de-id_20241011/). Federal guidance and terminology are distinguished here from Québec legislation.
