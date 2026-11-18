+++
title = "Technical evidence for legal assessment."
nav_label = "DPOs & lawyers"
kicker = "For data protection officers & legal professionals"
description = "Distinguish individual specificity, practical identifiability and sensitive-information disclosure when assessing brain imaging data."
updated = "18 November 2026"
+++
## Reference the relevant data type

Use the [consensus reference tables](consensus.html) to identify the exact representation, the paired ReID / technical SingleOut ratings, and the source qualifications. Direct links to individual entries can be recorded in a DPIA or disclosure assessment together with local conditions and safeguards. [How to cite a row](consensus.html#citing).

The four modality tables are available for [structural/diffusion imaging](consensus.html#structural), [functional imaging](consensus.html#functional), [PET](consensus.html#pet) and [EEG/MEG](consensus.html#eeg-meg). Classifications are technical evidence for a contextual assessment, not jurisdiction-independent legal decisions.

## Key messages

- **Specify the data representation and context.** “MRI data” could mean a full-head image, a cortical surface, regional measurements or a group result.
- **Separate technical findings from legal conclusions.** A successful match across scans, an unusual metadata record and identification of a person are different findings.
- **Evaluate the combined information.** Imaging, demographics, the reference population, available external data and access arrangements all belong in the assessment. [1, 2](#sources)

## Translate the technical terminology

| Term in the research | Technical question | Caution for interpretation |
| --- | --- | --- |
| Re-identification | Can research data be connected to a known identity? | State the external references and resources required |
| Individual specificity / technical “singling out” | Can records be distinguished, or matched across measurements? | This operational use in the manuscript is broader than legal identifiability |
| Record isolation in a table | Is a combination of values unique within the data? | Dataset uniqueness alone is not a complete legal test |
| Attribute disclosure | Can someone learn a sensitive fact about a person? | Disclosure can occur without locating one unique record |

The working manuscript explicitly limits its ratings to imaging-related properties. It is not a complete assessment of whether a particular release is anonymous under a jurisdiction's law. [2](#sources)

The [cross-jurisdiction glossary](glossary.html#singling-out) provides a vocabulary bridge for multidisciplinary discussions. Its purpose is to help researchers and participants interpret terms; it does not replace the applicable legal definitions. In particular, a HIPAA de-identification outcome is not automatically a GDPR anonymity outcome.

## What the imaging evidence establishes

MRI face-recognition studies demonstrate an identifiable pathway: sufficient facial information can be reconstructed and compared with identity-linked photographs. Brain-connectome fingerprinting studies instead demonstrate individual matching within research data. The availability of suitable identity-linked reference information is central to interpreting the latter as an identification scenario. [3, 4](#sources)

Acquisition coverage, resolution, processing and the population studied matter. Defacing and skull stripping alter the information available, but should not be treated as universal legal classifications. The working manuscript's assessment assumes direct identifiers have been removed and does not directly cover visually noticeable skull or brain abnormalities. [2](#sources)

## Metadata: identifiability and sensitivity differ

The published metaprivBIDS study screened participant metadata from selected OpenNeuro datasets and demonstrated complementary quantitative checks. It assessed potential vulnerabilities without attempting re-identification. Demographic combinations and location-related information were more important identification concerns than clinical scores in the analyses presented. [1](#sources)

This distinction matters: clinical information may be highly sensitive while contributing little to a matching process. Once another variable or external source enables a match, that information can still be disclosed. Conversely, a statistically unique record is not proof that an actor can connect it to a person. [1, 2](#sources)

k-anonymity, l-diversity, k-global, SUDA and PIF can help identify matters requiring investigation. They are not legal compliance certificates, and their values do not provide a universal re-identification probability or a jurisdiction-independent release threshold. [1](#sources)

## EU context: assess the relevant perspective

The EDPB's **Guidelines 02/2026, version 1.0**, adopted for public consultation on 7 July 2026, distinguish record isolation, linkage and inference. They call for assessment from the relevant entities' perspectives and of means reasonably likely to be used. Passing all three technical criteria supports anonymity; failure of one calls for further analysis rather than an automatic conclusion that the information is personal. [5](#sources)

In particular, the ability to isolate a record is not, by itself, equivalent to identifying its subject. The manuscript's technical “singling-out” ratings must therefore not be inserted directly into a GDPR determination. **An ordinal expert score is not an attack-success probability.** [2, 5](#sources)

This summary refers to the cited consultation version, not an assumed final or binding instrument. The applicable legal position, responsibilities and safeguards require assessment for the actual processing and jurisdiction.

## Pseudonymisation and recipient perspective

The revised manuscript glossary separates pseudonymisation from a conclusion about anonymity. A separately protected attribution key is a safeguard; it does not decide the status of every copy for every recipient. Record which entities can identify individuals using reasonably likely means and which additional information each can obtain. Do not infer that a recipient's inability to access the key alone settles all other routes to identification. [2, 5](#sources)

The manuscript's labels **Identifiable**, **Distinctive** and **Low likelihood** describe imaging-related evidence under stated assumptions. A distinctive pattern is not itself a finding of legal identifiability, and a low-likelihood label is not evidence of zero risk. [2](#sources)

## A useful joint assessment record

The following is an editorial checklist for discussions between imaging and legal teams, not a statutory form:

1. **Data and population:** specify files, processing level, metadata and any unusual clinical features.
2. **Actors and references:** identify recipients, access arrangements, possible external information and relevant capabilities.
3. **Evidence:** distinguish measured attack performance, expert judgement and untested possibilities; state study conditions.
4. **Safeguards:** describe technical measures, organisational controls, use conditions and residual assumptions.
5. **Scientific utility and change:** record the effects of transformations and when new evidence should trigger reassessment. [1, 2](#sources)

## Sources

1. Kibsgaard et al. (2026), [*Assessing metadata privacy in neuroimaging*](https://doi.org/10.1162/IMAG.a.1144). [Reproducible analyses](https://github.com/CPernet/OpenNeuro_MetaPrivAssessment).
2. Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*: completed manuscript consulted 18 November 2026; publication pending. [Associated analysis](https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io/tree/main/papers/expert-ratings).
3. Steeg et al. (2024), [MRI-derived face recognition](https://doi.org/10.1016/j.eclinm.2024.102930).
4. Finn et al. (2015), [functional-connectome fingerprinting](https://doi.org/10.1038/nn.4135).
5. EDPB, [*Guidelines 02/2026 on Anonymisation*, version 1.0](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202602_anonymisation_v1_en_0.pdf), adopted for public consultation 7 July 2026; see especially sections 2.4 and 3.5. [Publication and consultation context](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en).
