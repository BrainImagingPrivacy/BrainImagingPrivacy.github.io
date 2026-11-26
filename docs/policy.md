+++
title = "Policy grounded in imaging evidence."
nav_label = "Policymakers"
kicker = "For policymakers"
description = "Support useful data sharing with safeguards matched to the information, the research setting and the evidence."
updated = "26 November 2026"
+++
## The policy question

Sharing brain imaging data supports checking results and reusing existing research. Protecting participants requires understanding what the released information can reveal and under what conditions. A useful policy assessment therefore asks both **how a person could become identifiable** and **what protection would cost in scientific usefulness**. [1, 2](#sources)

## What the evidence says

**Brain imaging outputs differ.** Full-head images may retain recognisable facial information; a regional summary or connectivity matrix retains different features. The consensus preprint examines these representations separately, across modalities and processing levels. It focuses on imaging properties under stated assumptions rather than issuing a complete legal determination for every use. [2](#sources)

**Distinctiveness is not the same as recovering an identity.** Matching a person's brain-connectivity patterns across recordings is a demonstrated scientific capability. Whether this enables identification outside that research setting depends on additional information and opportunities for linkage. [2, 3](#sources)

**Accompanying tables deserve attention.** The metaprivBIDS paper found that age and demographic combinations were important potential identification routes in selected OpenNeuro metadata. Clinical scores contributed less to matching in these analyses while remaining sensitive if connected to a person. The study assessed potential vulnerabilities; it did not attempt to identify participants. [1](#sources)

## What these studies do not establish

They do not provide a universal probability of someone being identified from a brain scan. The metadata datasets were selected to cover different use cases, not to estimate the prevalence of privacy problems in all research data. The consensus manuscript uses expert judgements, with assumptions about the data and participants; its ordinal ratings are not percentages. [1, 2](#sources)

The manuscript's imaging assessment also does not automatically extend to people with visually noticeable skull or brain abnormalities, or to combinations with identifying metadata. A policy built around one modality-wide label would miss these conditions. [2](#sources)

## Implications for research policy

The following are implications drawn for this website from the two sources, rather than final recommendations endorsed by the consensus group.

| Policy priority | Practical implication |
| --- | --- |
| Assess complete releases | Include images, recordings, derivatives and accompanying metadata in disclosure review |
| Support proportionate access | Consider public and controlled access in relation to the actual information and intended use |
| Preserve scientific value | Test whether proposed coarsening, noise or image transformations affect the analyses the data should support |
| Resource the work | Provide time and expertise for curation, privacy assessment, documentation and maintenance |
| Make decisions reviewable | Record evidence, assumptions and reasons for revisiting an assessment |

The metadata paper illustrates why blanket removal of clinically valuable variables may target the wrong part of the problem. The contributors' knowledge of the study population and variables remains important alongside quantitative tools. [1](#sources)

## Make terminology travel with the data

International sharing needs more than a common label. Require teams to state what “anonymous”, “coded” or “de-identified” means under the relevant framework, which recipients were assessed, and what safeguards apply. The [glossary's jurisdiction comparison](glossary.html#de-identification) makes these differences accessible to researchers and participants; the labels do not establish equivalence between legal regimes.

The manuscript's revised distinction between record isolation, individual specificity and identifying a person supports this approach. Policies should also consider sensitive-attribute inference, even where recovering a name is unlikely. Synthetic data and federated analysis still need assessment of memorisation or output leakage. [2](#sources)

## Consult the dated evidence

The [consensus reference tables](consensus.html) make the completed manuscript's modality-specific ratings and qualifications available on the website. Policy documents can cite an individual entry and its source-check date rather than relying on a general label such as “brain data”.

## Keep the evidence current

New matching methods, accessible reference information and changing acquisition practices can alter an assessment. The website will accept studies and corrections through GitHub review, with a dated explanation when the guidance changes. New evidence should be evaluated for its study conditions and relevance, rather than automatically treated as proof that every dataset has the same risk. [2](#sources)

## Sources

1. **Published study:** Kibsgaard et al. (2026), [*Assessing metadata privacy in neuroimaging*](https://doi.org/10.1162/IMAG.a.1144). [OpenNeuro analysis notebooks](https://github.com/CPernet/OpenNeuro_MetaPrivAssessment).
2. **Preprint:** Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*. [arXiv:2611.32330](https://arxiv.org/abs/2611.32330), posted 24 November 2026. Website source consulted 18 November 2026. [Associated analysis](https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io/tree/main/papers/expert-ratings).
3. Finn et al. (2015), [*Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity*](https://doi.org/10.1038/nn.4135).
