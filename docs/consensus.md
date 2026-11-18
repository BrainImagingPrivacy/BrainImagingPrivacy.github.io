+++
title = "Consensus reference tables"
nav_label = "Consensus tables"
kicker = "For researchers, DPOs & governance teams"
description = "Imaging classifications, paired likelihood ratings, evidence and assessment considerations from the completed consensus manuscript."
updated = "18 November 2026"
status = "Completed manuscript · Publication pending"
evidence_note = "These tables reproduce the completed manuscript's classifications, ratings and qualifications. Website explanations are identified separately. The paper citation will be updated when publication details are available."
+++
## Use this reference {#use-this-reference}

This page brings the paper's four modality tables together so a proposed data release can be discussed without reopening the manuscript. Each data type has a permanent link, and the cited evidence is listed below. The [researcher page](researchers.html) explains assessment workflows; the [DPO page](legal.html) explains how the technical evidence fits a legal assessment.

**Source:** Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*. Completed manuscript, awaiting publication; tables checked against the source on **18 November 2026**. This page is a dated transcription, not a claim that the paper has been published or peer reviewed.

### Read the two ratings separately

**ReID** is the manuscript's re-identification likelihood rating. **SingleOut** is its technical singling-out rating: individual specificity and potential matching across recordings or datasets. This technical usage is not itself a finding of legal identifiability. See the [terminology and jurisdiction glossary](glossary.html#singling-out).

The numbers are **ordinal expert judgements on a 1–5 scale**, not measured attack probabilities: 4 does not mean an 80% chance of identification. A rating of **3** marks an undecided or context-dependent case in the manuscript; read the considerations alongside it. A low rating is not proof of zero risk.

| Classification in the paper | Meaning for this reference |
| --- | --- |
| **Identifiable** | Directly identifying features, or features considered likely to enable re-identification. |
| **Distinctive** | Individual-specific features permitting technical differentiation or matching; identity linkage and context still need assessment. |
| **Low likelihood** | Limited identification or individual-matching likelihood under the stated assumptions; not a guarantee of anonymity. |

### Scope that travels with the tables

The imaging assessment assumes **directly identifying metadata and annotations have been removed**, and concerns participants **without visually noticeable skull or brain abnormalities**. It does not directly cover unusual lesions or recognisable abnormalities. The tables do not evaluate the complete combination of imaging, demographic, behavioural and clinical information in a proposed release. Acquisition, processing, reference information, recipients and access arrangements can change the assessment.

Classification alone is neither permission to release data nor a jurisdiction-independent legal determination. Record the relevant source row, local conditions and safeguards in the assessment. The paper distinguishes technical individuality from identification, and recommends revisiting assessments as methods and reference datasets change.

## Find a modality {#modalities}

- [Structural MRI, CT and diffusion — paper Table 2](#structural)
- [Functional imaging: BOLD, ASL and fNIRS — paper Table 3](#functional)
- [PET — paper Table 4](#pet)
- [EEG and MEG — paper Table 5](#eeg-meg)
- [Rating correlations — paper Table 1](#rating-correlations)

The **data-type labels, class assignments, paired values and substantive qualifications** below follow the source. Line breaks are reformatted for the web. Empty evidence cells are marked explicitly. Shared cells are expanded without inventing new ratings.


## Structural MRI, CT and diffusion {#structural}

**Table 2 of the manuscript.** Data-type names link directly to the corresponding entry.

**Diffusion distinction:** clinical DWI here means typical few-direction clinical acquisitions. Research dMRI means higher-resolution, many-direction and potentially multishell acquisitions. They are separate entries, not interchangeable labels.

| Data type and classification | ReID | SingleOut | Evidence and considerations |
| --- | --- | --- | --- |
| <span id="raw-structural"></span>[Raw structural MRI<br>Raw structural CT](#raw-structural)<br>**IDENTIFIABLE** | 4.0 | 5.0 | If coverage is extensive enough, it can be matched to photographs with regular face recognition software ([Schwarz et al., 2019](#ref-schwarz-2019); [Steeg et al., 2024](#ref-steeg-2024))<br><br>**Considerations:** Assuming research data quality images with full head coverage and high resolution |
| <span id="defaced-structural"></span>[Face removed raw structural data (MRI, CT)](#defaced-structural)<br>**DISTINCTIVE** | 2.0 | 4.0 | Depends on whether ears and teeth are present; reverse reconstruction can be done ([Abramian &amp; Eklund, 2019](#ref-abramian-2019); [Y. Xiao et al., 2022](#ref-xiao-2022))<br><br>**Considerations:** No face blurring; removal should apply. No bone abnormalities should be visible. |
| <span id="skull-stripped-structural"></span>[Skull-stripped raw structural data (MRI, CT)](#skull-stripped-structural)<br>**DISTINCTIVE** | 2.0 | 4.0 | Subject-specific ([Takao et al., 2015](#ref-takao-2015)) |
| <span id="tissue-maps"></span>[Tissue maps (scalp, skull, GM, WM, CSF), VBM, SDM](#tissue-maps)<br>**DISTINCTIVE** | 2.0 | 4.0 | Subject-specific ([Takao et al., 2015](#ref-takao-2015)) |
| <span id="morphometric-maps"></span>[Morphometric maps (thickness, curvature, etc)](#morphometric-maps)<br>**DISTINCTIVE** | 2.5 | 4.0 | High single-out rate ([Duan et al., 2019](#ref-duan-2019); [Guillon et al., 2024](#ref-guillon-2024); [Mansour L et al., 2021](#ref-mansour-l-2021); [Wachinger et al., 2015](#ref-wachinger-2015)) |
| <span id="morphometric-models"></span>[Morphometric models (e.g. cortical mesh)](#morphometric-models)<br>**DISTINCTIVE** | 2.0 | 3.0 | High single-out rate ([Duan et al., 2019](#ref-duan-2019); [Guillon et al., 2024](#ref-guillon-2024); [Mansour L et al., 2021](#ref-mansour-l-2021); [Wachinger et al., 2015](#ref-wachinger-2015))<br><br>**Considerations:** Consider the image and mesh resolutions. |
| <span id="synthetic-same-modality"></span>[Synthetic images for the same imaging type (e.g. learn from T1w, make T1w)](#synthetic-same-modality)<br>**DISTINCTIVE** | 2.0 | 3.0 | A generative model can memorise images ([Dar et al., 2025](#ref-dar-2025); [Usman Akbar et al., 2025](#ref-usman-akbar-2025))<br><br>**Considerations:** AI model leakage must be assessed. |
| <span id="synthetic-cross-modality"></span>[Synthetic images for different imaging types (e.g learn from MRI, make CT; learn from T1w, make T2w)](#synthetic-cross-modality)<br>**LOW LIKELIHOOD** | 2.0 | 2.0 | A generative model can memorise images ([Dar et al., 2025](#ref-dar-2025); [Usman Akbar et al., 2025](#ref-usman-akbar-2025))<br><br>**Considerations:** Currently not as accurate as generative models from the same modality, but leakage should be checked |
| <span id="regional-morphometry"></span>[Table of morphometric (volume, thickness, etc.) or qMRI (T1 time) ROI information](#regional-morphometry)<br>**DISTINCTIVE** | 1.0 | 3.0 | Brains have unique patterns, such that one can single out subjects ([Valizadeh et al., 2018](#ref-valizadeh-2018))<br><br>**Considerations:** It is important to consider the number of features (and quality) |
| <span id="clinical-dwi"></span>[Raw DWI](#clinical-dwi)<br>**LOW LIKELIHOOD** | 2.5 | 2.0 | Re-ID has not been demonstrated successfully ([Schwarz et al., 2023](#ref-schwarz-2023)). |
| <span id="research-dmri"></span>[Raw dMRI](#research-dmri)<br>**DISTINCTIVE** | 2.5 | 4 | Re-ID has not been demonstrated successfully ([Schwarz et al., 2023](#ref-schwarz-2023)). |
| <span id="diffusion-metrics"></span>[Derived Diffusion Metrics (e.g. ADC, FA, MD)](#diffusion-metrics)<br>**LOW LIKELIHOOD** | 1.0 | 2.5 | Track specific features ([D. Wang et al., 2023](#ref-wang-2023)) |
| <span id="dmri-connectivity"></span>[dMRI connectivity matrices](#dmri-connectivity)<br>**DISTINCTIVE** | 2.0 | 4 | Connectome can single out individuals ([Ciarrusta et al., 2022](#ref-ciarrusta-2022); [Mansour L et al., 2021](#ref-mansour-l-2021); [Yeh et al., 2016](#ref-yeh-2016)) |

## Functional imaging: BOLD, ASL and fNIRS {#functional}

**Table 3 of the manuscript.** Data-type names link directly to the corresponding entry.

**Preprocessed ASL/BOLD:** the source assigns different classes to ASL and BOLD but prints one shared rating pair. That pair is retained below, rather than inferring separate ASL values. Normalisation and smoothing must be considered.

| Data type and classification | ReID | SingleOut | Evidence and considerations |
| --- | --- | --- | --- |
| <span id="raw-fmri"></span>[Raw fMRI](#raw-fmri)<br>**DISTINCTIVE** | 2.0 | 3.0 | Face may be visible for very high resolution and high field, but has not been demonstrated successfully ([Schwarz et al., 2023](#ref-schwarz-2023))<br><br>**Considerations:** Consider the scanner field strength and voxel resolution |
| <span id="raw-asl"></span>[Raw ASL](#raw-asl)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |
| <span id="preprocessed-bold-asl"></span>[Preprocessed data](#preprocessed-bold-asl)<br>**LOW LIKELIHOOD for ASL; DISTINCTIVE for BOLD** | 1.0 | 3 | Brain images retain their main distinguishing information and features ([Chen et al., 2013](#ref-chen-2013))<br><br>**Considerations:** Consider if images are spatially normalised and smoothed<br>**Shared source pair:** ASL and BOLD values are not separated in the manuscript. |
| <span id="perfusion-flow"></span>[Other perfusion (CE) and Flow imaging (TOF)](#perfusion-flow)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |
| <span id="mrs"></span>[MRS](#mrs)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |
| <span id="activation-maps"></span>[Task-based activation maps](#activation-maps)<br>**LOW LIKELIHOOD** | 1.0 | 2 | Activation patterns can be stable within a subject ([Gorgolewski et al., 2012](#ref-gorgolewski-2012)) but are highly task and motion dependent ([Gorgolewski et al., 2013](#ref-gorgolewski-2013)) |
| <span id="regional-time-series"></span>[Raw or minimally processed time series (fMRI, ASL, fNIRS)](#regional-time-series)<br>**LOW LIKELIHOOD** | 2.0 | 2.0 | A single regional time course is unique enough to single out ([Zhang &amp; Li, 2024](#ref-zhang-2024)) |
| <span id="participant-decompositions"></span>[Participant-specific ICA and other decomposition outputs](#participant-decompositions)<br>**DISTINCTIVE** | 1.5 | 3.0 | Network-specific, like connectivity matrices ([N. Wang et al., 2017](#ref-wang-2017); [X. Wang et al., 2025](#ref-wang-2025); [Xie et al., 2018](#ref-xie-2018))<br><br>**Considerations:** Distinguish participant-specific outputs from group-level component maps. |
| <span id="bold-connectivity"></span>[BOLD connectivity matrices](#bold-connectivity)<br>**DISTINCTIVE** | 2.0 | 4.0 | Connectomes are unique, even at low resolution ([Amico &amp; Goñi, 2018](#ref-amico-2018); [Byrge &amp; Kennedy, 2019](#ref-byrge-2019); [Finn et al., 2015](#ref-finn-2015); [Miranda-Dominguez et al., 2014](#ref-miranda-dominguez-2014); [Van De Ville et al., 2021](#ref-van-de-ville-2021)). The connectivity pattern allows cross-database singling out ([Ravindra et al., 2021](#ref-ravindra-2021); [Ravindra &amp; Grama, 2019](#ref-ravindra-2019)) |
| <span id="fnirs-connectivity"></span>[fNIRS connectivity](#fnirs-connectivity)<br>**DISTINCTIVE** | 2.0 | 3.0 | Sensor-level ([Ren et al., 2022](#ref-ren-2022); [Rodrigues et al., 2019](#ref-rodrigues-2019)) connectivity is good enough to single out individuals |
| <span id="connectivity-summaries"></span>[Connectivity summaries (graph-derived metrics, dynamical measures like dwell time, etc)](#connectivity-summaries)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |
| <span id="group-connectivity"></span>[Summary connectivity maps and group matrices](#group-connectivity)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |

## Positron emission tomography {#pet}

**Table 4 of the manuscript.** Data-type names link directly to the corresponding entry.

**Raw PET:** the paper calls for considering scanner resolution, reconstruction, tracer and dose, and testing facial reconstruction. Where facial identifiability remains in doubt, its discussion recommends removing the face.

| Data type and classification | ReID | SingleOut | Evidence and considerations |
| --- | --- | --- | --- |
| <span id="raw-pet"></span>[Raw PET images](#raw-pet)<br>**DISTINCTIVE** | 3.0 | 3.0 | Face can be seen depending on the tracer ([Bou Hanna et al., 2024](#ref-bou-hanna-2024); [Schwarz et al., 2022](#ref-schwarz-2022); [Selfridge et al., 2023](#ref-selfridge-2023))<br><br>**Considerations:** Consider scanner resolution, image reconstruction, tracer, and dose, and test face reconstruction. |
| <span id="pet-parametric"></span>[Parametric maps (e.g., SUV, SUVR, DVR, VT, KI) and kinetic parameters](#pet-parametric)<br>**LOW LIKELIHOOD** | 1.0 | 2.0 | No specific evidence citation in the source table. |
| <span id="pet-connectivity"></span>[PET connectivity matrices](#pet-connectivity)<br>**LOW LIKELIHOOD** | 2.0 | 2.5 | No specific evidence citation in the source table. |

## EEG and MEG electrophysiology {#eeg-meg}

**Table 5 of the manuscript.** Data-type names link directly to the corresponding entry.

**Shared source cells:** the paper shares the evidence and ReID **2.0** / SingleOut **3.0** across raw/preprocessed signals and single-trial time courses or features. Both rows show that shared information explicitly here.

| Data type and classification | ReID | SingleOut | Evidence and considerations |
| --- | --- | --- | --- |
| <span id="raw-eeg-meg"></span>[Raw and preprocessed signals](#raw-eeg-meg)<br>**DISTINCTIVE** | 2.0 | 3.0 | Contains unique features (also in the non-brain signals such as eye blinks, muscle activity), allowing one to single out individuals ([da Silva Castanheira et al., 2021](#ref-da-silva-castanheira-2021); [Liu et al., 2024](#ref-liu-2024); [Meng et al., 2024](#ref-meng-2024); [Sareen et al., 2021](#ref-sareen-2021); [Wu et al., 2022](#ref-wu-2022))<br>Evidence and ratings are shared across these two rows in the manuscript. |
| <span id="single-trial"></span>[Single-trial time courses or features](#single-trial)<br>**DISTINCTIVE** | 2.0 | 3.0 | Contains unique features (also in the non-brain signals such as eye blinks, muscle activity), allowing one to single out individuals ([da Silva Castanheira et al., 2021](#ref-da-silva-castanheira-2021); [Liu et al., 2024](#ref-liu-2024); [Meng et al., 2024](#ref-meng-2024); [Sareen et al., 2021](#ref-sareen-2021); [Wu et al., 2022](#ref-wu-2022))<br>Evidence and ratings are shared across these two rows in the manuscript. |
| <span id="power-spectrum"></span>[Power spectrum](#power-spectrum)<br>**DISTINCTIVE** | 2.5 | 4.0 | Within session highly subject-specific ([Castanheira et al., 2025](#ref-castanheira-2025); [Demuru &amp; Fraschini, 2020](#ref-demuru-2020); [Jijomon &amp; Vinod, 2018](#ref-jijomon-2018); [Stergiadis et al., 2022](#ref-stergiadis-2022); [Suppiah &amp; Vinod, 2018](#ref-suppiah-2018); [Tatar, 2023](#ref-tatar-2023); [Thomas &amp; Vinod, 2017](#ref-thomas-2017)) and matching across independently acquired sessions ([da Silva Castanheira et al., 2021](#ref-da-silva-castanheira-2021); [DelPozo-Banos et al., 2015](#ref-delpozo-banos-2015)) |
| <span id="evoked-responses"></span>[ERP/EFP](#evoked-responses)<br>**DISTINCTIVE** | 1.0 | 3.0 | ERPs are highly reliable within subjects ([Cassidy et al., 2012](#ref-cassidy-2012); [Gaspar et al., 2011](#ref-gaspar-2011)) but moderately stable over time ([Weinberg &amp; Hajcak, 2011](#ref-weinberg-2011))<br><br>**Considerations:** Depends highly on the stimulus type used |
| <span id="eeg-meg-connectivity"></span>[MEEG connectivity matrices](#eeg-meg-connectivity)<br>**DISTINCTIVE** | 2.0 | 4.0 | connectome can single out individuals ([da Silva Castanheira et al., 2021](#ref-da-silva-castanheira-2021); [Fraschini et al., 2015](#ref-fraschini-2015); [Kong et al., 2019](#ref-kong-2019); [Rocca et al., 2014](#ref-rocca-2014)) |

## Rating correlations — paper Table 1 {#rating-correlations}

This methodological table concerns the association between **expert ratings**, not probabilities of attack success. The number of data points is the number of ratings across items, not a participant count. The paper reports an overall Spearman correlation of 0.628 (p < 0.001); the modality-level results below reproduce Table 1.

| Imaging class | Rating data points | Spearman correlation | FDR-corrected p-value |
| --- | --- | --- | --- |
| Structural Images | 162 | 0.562 | &lt;0.001 |
| Dynamic Imaging (BOLD, ASL) | 126 | 0.656 | &lt;0.001 |
| Diffusion Imaging | 27 | 0.502 | 0.011 |
| PET | 27 | 0.468 | 0.016 |
| Electrophysiology (MEEG) | 90 | 0.588 | &lt;0.001 |
| fNIRS | 18 | 0.449 | 0.061 |
| Connectivity | 117 | 0.680 | &lt;0.001 |

## Refer to a row in an assessment {#citing}

Use the modality heading or an individual data-type link to share the exact entry. For a dated assessment, record:

> Pernet et al., *An expert consensus on identification likelihood in NeuroImaging data*, completed manuscript (publication pending). Brain Imaging Privacy consensus reference tables, source checked 18 November 2026, paper Table [number], data type [name]. Accessed [date].

The corresponding Markdown is versioned in [the website repository](https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io/blob/main/docs/consensus.md). Its Git history provides a record of changes. Once the paper is public, its DOI or preprint link should replace the publication-pending citation; none is invented here.

## Evidence cited in the modality tables {#evidence}

These references are transcribed from the manuscript's bibliography and linked to their recorded DOI or source URL. Including a reference reports the paper's evidential basis; it is not a claim that every cited study measured real-world re-identification.


<span id="ref-abramian-2019"></span>

Abramian, D., &amp; Eklund, A. (2019). Refacing: Reconstructing Anonymized Facial Features Using GANS. 2019 IEEE 16th International Symposium on Biomedical Imaging (ISBI 2019), 1104–1108. [Source](https://doi.org/10.1109/ISBI.2019.8759515)


<span id="ref-amico-2018"></span>

Amico, E., &amp; Goñi, J. (2018). The quest for identifiability in human functional connectomes. Scientific Reports, 8(1), 8254. [Source](https://doi.org/10.1038/s41598-018-25089-1)


<span id="ref-bou-hanna-2024"></span>

Bou Hanna, E., Partarrieu, S., Berenbaum, A., Allassonnière, S., &amp; Besson, F. L. (2024). Exploring de-anonymization risks in PET imaging: Insights from a comprehensive analysis of 853 patient scans. Scientific Data, 11(1), 932. [Source](https://doi.org/10.1038/s41597-024-03800-4)


<span id="ref-byrge-2019"></span>

Byrge, L., &amp; Kennedy, D. P. (2019). High-accuracy individual identification using a “thin slice” of the functional connectome. Network Neuroscience, 3(2), 363–383. [Source](https://doi.org/10.1162/netn_a_00068)


<span id="ref-cassidy-2012"></span>

Cassidy, S. M., Robertson, I. H., &amp; O’Connell, R. G. (2012). Retest reliability of event-related potentials: Evidence from a variety of paradigms. Psychophysiology, 49(5), 659–664. [Source](https://doi.org/10.1111/j.1469-8986.2011.01349.x)


<span id="ref-castanheira-2025"></span>

Castanheira, J. da S., Wiesman, A. I., Taylor, M. J., &amp; Baillet, S. (2025). The lifespan evolution of individualized neurophysiological traits. Cell Reports, 44(12). [Source](https://doi.org/10.1016/j.celrep.2025.116657)


<span id="ref-chen-2013"></span>

Chen, F., Su, L., Liu, Y., &amp; Hu, D. (2013). Confirming the Diversity of the Brain after Normalization: An Approach Based on Identity Authentication. PLOS ONE, 8(1), e54328. [Source](https://doi.org/10.1371/journal.pone.0054328)


<span id="ref-ciarrusta-2022"></span>

Ciarrusta, J., Christiaens, D., Fitzgibbon, S. P., Dimitrova, R., Hutter, J., Hughes, E., Duff, E., Price, A. N., Cordero-Grande, L., Tournier, J.-D., Rueckert, D., Hajnal, J. V., Arichi, T., McAlonan, G., Edwards, A. D., &amp; Batalle, D. (2022). The developing brain structural and functional connectome fingerprint. Developmental Cognitive Neuroscience, 55, 101117. [Source](https://doi.org/10.1016/j.dcn.2022.101117)


<span id="ref-da-silva-castanheira-2021"></span>

da Silva Castanheira, J., Orozco Perez, H. D., Misic, B., &amp; Baillet, S. (2021). Brief segments of neurophysiological activity enable individual differentiation. Nature Communications, 12(1), 5713. [Source](https://doi.org/10.1038/s41467-021-25895-8)


<span id="ref-dar-2025"></span>

Dar, S. U. H., Seyfarth, M., Ayx, I., Papavassiliu, T., Schoenberg, S. O., Siepmann, R. M., Laqua, F. C., Kahmann, J., Frey, N., Baeßler, B., Foersch, S., Truhn, D., Kather, J. N., &amp; Engelhardt, S. (2025). Unconditional latent diffusion models memorize patient imaging data. Nature Biomedical Engineering, 1–15. [Source](https://doi.org/10.1038/s41551-025-01468-8)


<span id="ref-delpozo-banos-2015"></span>

DelPozo-Banos, M., Travieso, C. M., Weidemann, C. T., &amp; Alonso, J. B. (2015). EEG biometric identification: A thorough exploration of the time-frequency domain. Journal of Neural Engineering, 12(5), 056019. [Source](https://doi.org/10.1088/1741-2560/12/5/056019)


<span id="ref-demuru-2020"></span>

Demuru, M., &amp; Fraschini, M. (2020). EEG fingerprinting: Subject-specific signature based on the aperiodic component of power spectrum. Computers in Biology and Medicine, 120, 103748. [Source](https://doi.org/10.1016/j.compbiomed.2020.103748)


<span id="ref-duan-2019"></span>

Duan, D., Xia, S., Wu, Z., Wang, F., Wang, L., Lin, W., Gilmore, J. H., Shen, D., &amp; Li, G. (2019). CORTICAL FOLDINGPRINTS FOR INFANT IDENTIFICATION. Proceedings. IEEE International Symposium on Biomedical Imaging, 2019, 396–399. [Source](https://doi.org/10.1109/ISBI.2019.8759429)


<span id="ref-finn-2015"></span>

Finn, E. S., Shen, X., Scheinost, D., Rosenberg, M. D., Huang, J., Chun, M. M., Papademetris, X., &amp; Constable, R. T. (2015). Functional connectome fingerprinting: Identifying individuals using patterns of brain connectivity. Nature Neuroscience, 18(11), 1664–1671. [Source](https://doi.org/10.1038/nn.4135)


<span id="ref-fraschini-2015"></span>

Fraschini, M., Hillebrand, A., Demuru, M., Didaci, L., &amp; Marcialis, G. L. (2015). An EEG-Based Biometric System Using Eigenvector Centrality in Resting State Brain Networks. IEEE Signal Processing Letters, 22(6), 666–670. [Source](https://doi.org/10.1109/LSP.2014.2367091)


<span id="ref-gaspar-2011"></span>

Gaspar, C. M., Rousselet, G. A., &amp; Pernet, C. R. (2011). Reliability of ERP and single-trial analyses. NeuroImage, 58(2), 620–629. [Source](https://doi.org/10.1016/j.neuroimage.2011.06.052)


<span id="ref-gorgolewski-2012"></span>

Gorgolewski, K. J., Storkey, A. J., Bastin, M. E., &amp; Pernet, C. R. (2012). Adaptive thresholding for reliable topological inference in single subject fMRI analysis. Frontiers in Human Neuroscience, 6. [Source](https://doi.org/10.3389/fnhum.2012.00245)


<span id="ref-gorgolewski-2013"></span>

Gorgolewski, K. J., Storkey, A. J., Bastin, M. E., Whittle, I., &amp; Pernet, C. (2013). Single subject fMRI test–retest reliability metrics and confounding factors. NeuroImage, 69, 231–243. [Source](https://doi.org/10.1016/j.neuroimage.2012.10.085)


<span id="ref-guillon-2024"></span>

Guillon, L., Chavas, J., Bénézit, A., Moutard, M.-L., Roca, P., Mellerio, C., Oppenheim, C., Rivière, D., &amp; Mangin, J.-F. (2024). Identification of rare cortical folding patterns using unsupervised deep learning. Imaging Neuroscience, 2, imag–2–00084. [Source](https://doi.org/10.1162/imag_a_00084)


<span id="ref-jijomon-2018"></span>

Jijomon, C. M., &amp; Vinod, A. P. (2018). EEG-based Biometric Identification using Frequently Occurring Maximum Power Spectral Features. 2018 IEEE Applied Signal Processing Conference (ASPCON), 249–252. [Source](https://doi.org/10.1109/ASPCON.2018.8748581)


<span id="ref-kong-2019"></span>

Kong, W., Wang, L., Xu, S., Babiloni, F., &amp; Chen, H. (2019). EEG Fingerprints: Phase Synchronization of EEG Signals as Biomarker for Subject Identification. IEEE Access, 7, 121165–121173. [Source](https://doi.org/10.1109/ACCESS.2019.2931624)


<span id="ref-liu-2024"></span>

Liu, H., Jin, X., Liu, D., Kong, W., Tang, J., &amp; Peng, Y. (2024). Affective EEG-based cross-session person identification using hierarchical graph embedding. Cognitive Neurodynamics, 18(5), 2897–2908. [Source](https://doi.org/10.1007/s11571-024-10132-x)


<span id="ref-mansour-l-2021"></span>

Mansour L, S., Tian, Y., Yeo, B. T. T., Cropley, V., &amp; Zalesky, A. (2021). High-resolution connectomic fingerprints: Mapping neural identity and behavior. NeuroImage, 229, 117695. [Source](https://doi.org/10.1016/j.neuroimage.2020.117695)


<span id="ref-meng-2024"></span>

Meng, L., Jiang, X., Jia, T., &amp; Wu, D. (2024). Protecting Multiple Types of Privacy Simultaneously in EEG-based Brain-Computer Interfaces (arXiv:2411.19498). arXiv. [Source](https://doi.org/10.48550/arXiv.2411.19498)


<span id="ref-miranda-dominguez-2014"></span>

Miranda-Dominguez, O., Mills, B. D., Carpenter, S. D., Grant, K. A., Kroenke, C. D., Nigg, J. T., &amp; Fair, D. A. (2014). Connectotyping: Model Based Fingerprinting of the Functional Connectome. PLOS ONE, 9(11), e111048. [Source](https://doi.org/10.1371/journal.pone.0111048)


<span id="ref-ravindra-2019"></span>

Ravindra, V., &amp; Grama, A. (2019). De-anonymization Attacks on Neuroimaging Datasets. arXiv:1908.03260 [Cs, Eess, q-Bio]. [Source](http://arxiv.org/abs/1908.03260)


<span id="ref-ravindra-2021"></span>

Ravindra, V., Drineas, P., &amp; Grama, A. (2021). Constructing Compact Signatures for Individual Fingerprinting of Brain Connectomes. Frontiers in Neuroscience, 15. [Source](https://doi.org/10.3389/fnins.2021.549322)


<span id="ref-ren-2022"></span>

Ren, H., Zhou, S., Zhang, L., Zhao, F., &amp; Qiao, L. (2022). Identifying Individuals by fNIRS-Based Brain Functional Network Fingerprints. Frontiers in Neuroscience, 16. [Source](https://doi.org/10.3389/fnins.2022.813293)


<span id="ref-rocca-2014"></span>

Rocca, D. L., Campisi, P., Vegso, B., Cserti, P., Kozmann, G., Babiloni, F., &amp; Fallani, F. D. V. (2014). Human brain distinctiveness based on EEG spectral coherence connectivity. IEEE Transactions on Bio-Medical Engineering, 61(9), 2406–2412. [Source](https://doi.org/10.1109/TBME.2014.2317881)


<span id="ref-rodrigues-2019"></span>

Rodrigues, J. de S., Ribeiro, F. L., Sato, J. R., Mesquita, R. C., &amp; Júnior, C. E. B. (2019). Identifying individuals using fNIRS-based cortical connectomes. Biomedical Optics Express, 10(6), 2889–2897. [Source](https://doi.org/10.1364/BOE.10.002889)


<span id="ref-sareen-2021"></span>

Sareen, E., Zahar, S., Ville, D. V. D., Gupta, A., Griffa, A., &amp; Amico, E. (2021). Exploring MEG brain fingerprints: Evaluation, pitfalls, and interpretations. NeuroImage, 240, 118331. [Source](https://doi.org/10.1016/j.neuroimage.2021.118331)


<span id="ref-schwarz-2019"></span>

Schwarz, C. G., Kremers, W. K., Therneau, T. M., Sharp, R. R., Gunter, J. L., Vemuri, P., Arani, A., Spychalla, A. J., Kantarci, K., Knopman, D. S., Petersen, R. C., &amp; Jack, C. R. (2019). Identification of Anonymous MRI Research Participants with Face-Recognition Software. New England Journal of Medicine, 381(17), 1684–1686. [Source](https://doi.org/10.1056/NEJMc1908881)


<span id="ref-schwarz-2022"></span>

Schwarz, C. G., Kremers, W. K., Lowe, V. J., Savvides, M., Gunter, J. L., Senjem, M. L., Vemuri, P., Kantarci, K., Knopman, D. S., Petersen, R. C., &amp; Jack, C. R. (2022). Face recognition from research brain PET: An unexpected PET problem. NeuroImage, 258, 119357. [Source](https://doi.org/10.1016/j.neuroimage.2022.119357)


<span id="ref-schwarz-2023"></span>

Schwarz, C. G., Kremers, W. K., Arani, A., Savvides, M., Reid, R. I., Gunter, J. L., Senjem, M. L., Cogswell, P. M., Vemuri, P., Kantarci, K., Knopman, D. S., Petersen, R. C., Jack, C. R., &amp; Alzheimer’s Disease Neuroimaging Initiative. (2023). A face-off of MRI research sequences by their need for de-facing. NeuroImage, 276, 120199. [Source](https://doi.org/10.1016/j.neuroimage.2023.120199)


<span id="ref-selfridge-2023"></span>

Selfridge, A. R., Spencer, B. A., Abdelhafez, Y. G., Nakagawa, K., Tupin, J. D., &amp; Badawi, R. D. (2023). Facial Anonymization and Privacy Concerns in Total-Body PET/CT. Journal of Nuclear Medicine, 64(8), 1304–1309. [Source](https://doi.org/10.2967/jnumed.122.265280)


<span id="ref-steeg-2024"></span>

Steeg, K., Bohrer, E., Schäfer, S. B., Vu, V. D., Scherberich, J., Windfelder, A. G., &amp; Krombach, G. A. (2024). Re-identification of anonymised MRI head images with publicly available software: Investigation of the current risk to patient privacy. eClinicalMedicine, 78. [Source](https://doi.org/10.1016/j.eclinm.2024.102930)


<span id="ref-stergiadis-2022"></span>

Stergiadis, C., Kostaridou, V.-D., Veloudis, S., Kazis, D., &amp; Klados, M. A. (2022). A Personalized User Authentication System Based on EEG Signals. Sensors, 22(18), 6929. [Source](https://doi.org/10.3390/s22186929)


<span id="ref-suppiah-2018"></span>

Suppiah, R., &amp; Vinod, A. P. (2018). Biometric identification using single channel EEG during relaxed resting state. IET Biometrics, 7(4), 342–348. [Source](https://doi.org/10.1049/iet-bmt.2017.0142)


<span id="ref-takao-2015"></span>

Takao, H., Hayashi, N., &amp; Ohtomo, K. (2015). Brain morphology is individual-specific information. Magnetic Resonance Imaging, 33(6), 816–821. [Source](https://doi.org/10.1016/j.mri.2015.03.010)


<span id="ref-tatar-2023"></span>

Tatar, A. B. (2023). Biometric identification system using EEG signals. Neural Computing and Applications, 35(1), 1009–1023. [Source](https://doi.org/10.1007/s00521-022-07795-0)


<span id="ref-thomas-2017"></span>

Thomas, K. P., &amp; Vinod, A. P. (2017). Toward EEG-Based Biometric Systems: The Great Potential of Brain-Wave-Based Biometrics. IEEE Systems, Man, and Cybernetics Magazine, 3(4), 6–15. [Source](https://doi.org/10.1109/MSMC.2017.2703651)


<span id="ref-usman-akbar-2025"></span>

Usman Akbar, M., Wang, W., &amp; Eklund, A. (2025). Beware of diffusion models for synthesizing medical images—A comparison with GANs in terms of memorizing brain MRI and chest x-ray images. Machine Learning: Science and Technology, 6(1), 015022. [Source](https://doi.org/10.1088/2632-2153/ad9a3a)


<span id="ref-valizadeh-2018"></span>

Valizadeh, S. A., Liem, F., Mérillat, S., Hänggi, J., &amp; Jäncke, L. (2018). Identification of individual subjects on the basis of their brain anatomical features. Scientific Reports, 8(1), 5611. [Source](https://doi.org/10.1038/s41598-018-23696-6)


<span id="ref-van-de-ville-2021"></span>

Van De Ville, D., Farouj, Y., Preti, M. G., Liégeois, R., &amp; Amico, E. (2021). When makes you unique: Temporality of the human brain fingerprint. Science Advances, 7(42), eabj0751. [Source](https://doi.org/10.1126/sciadv.abj0751)


<span id="ref-wachinger-2015"></span>

Wachinger, C., Golland, P., Kremen, W., Fischl, B., Reuter, M., &amp; Alzheimer’s Disease Neuroimaging Initiative. (2015). BrainPrint: A discriminative characterization of brain morphology. NeuroImage, 109, 232–248. [Source](https://doi.org/10.1016/j.neuroimage.2015.01.032)


<span id="ref-wang-2017"></span>

Wang, N., Chang, C., Zeng, W., Shi, Y., &amp; Yan, H. (2017). A Novel Feature-Map Based ICA Model for Identifying the Individual, Intra/Inter-Group Brain Networks across Multiple fMRI Datasets. Frontiers in Neuroscience, 11, 510. [Source](https://doi.org/10.3389/fnins.2017.00510)


<span id="ref-wang-2023"></span>

Wang, D., Fan, Q., Xiao, X., He, H., Yang, Y., &amp; Li, Y. (2023). Structural Fingerprinting of the Frontal Aslant Tract: Predicting Cognitive Control Capacity and Obsessive-Compulsive Symptoms. The Journal of Neuroscience, 43(42), 7016–7027. [Source](https://doi.org/10.1523/JNEUROSCI.0628-23.2023)


<span id="ref-wang-2025"></span>

Wang, X., Zou, T., Wang, H., Han, H., Chen, H., Calhoun, V. D., &amp; Li, R. (2025). A dynamic spatiotemporal representation framework for deciphering personal brain function. NeuroImage, 319, 121443. [Source](https://doi.org/10.1016/j.neuroimage.2025.121443)


<span id="ref-weinberg-2011"></span>

Weinberg, A., &amp; Hajcak, G. (2011). Longer term test-retest reliability of error-related brain activity. Psychophysiology, 48(10), 1420–1425. [Source](https://doi.org/10.1111/j.1469-8986.2011.01206.x)


<span id="ref-wu-2022"></span>

Wu, S., Ramdas, A., &amp; Wehbe, L. (2022). Brainprints: Identifying individuals from magnetoencephalograms. Communications Biology, 5(1), 852. [Source](https://doi.org/10.1038/s42003-022-03727-9)


<span id="ref-xiao-2022"></span>

Xiao, Y., Ashbee, W., Calhoun, V. D., &amp; Plis, S. (2022). Refacing Defaced MRI with PixelCNN. 2022 International Joint Conference on Neural Networks (IJCNN), 1–7. [Source](https://doi.org/10.1109/IJCNN55064.2022.9891937)


<span id="ref-xie-2018"></span>

Xie, H., Calhoun, V. D., Gonzalez-Castillo, J., Damaraju, E., Miller, R., Bandettini, P. A., &amp; Mitra, S. (2018). Whole-brain connectivity dynamics reflect both task-specific and individual-specific modulation: A multitask study. NeuroImage, 180(Pt B), 495–504. [Source](https://doi.org/10.1016/j.neuroimage.2017.05.050)


<span id="ref-yeh-2016"></span>

Yeh, F.-C., Vettel, J. M., Singh, A., Poczos, B., Grafton, S. T., Erickson, K. I., Tseng, W.-Y. I., &amp; Verstynen, T. D. (2016). Quantifying Differences and Similarities in Whole-Brain White Matter Architecture Using Local Connectome Fingerprints. PLOS Computational Biology, 12(11), e1005203. [Source](https://doi.org/10.1371/journal.pcbi.1005203)


<span id="ref-zhang-2024"></span>

Zhang, Y., &amp; Li, J. (2024). Identification of individuals using functional near-infrared spectroscopy based on a one-dimensional convolutional neural network. Journal of Biophotonics, 17(3), e202300453. [Source](https://doi.org/10.1002/jbio.202300453)


## Editorial provenance {#provenance}

Transcribed from the completed manuscript's main Tables 1–5 on 18 November 2026. Earlier item-generation tables in the annexes are not substituted for the consensus tables. Numerical values and class labels are retained; repeated merged cells are expanded. The typo “fNRIS” is normalised to “fNIRS”; a terminal decimal point in the task-activation SingleOut value is formatted as 2. Other source nomenclature, including “ERP/EFP”, is retained. The ASL/BOLD shared pair is labelled rather than silently resolved. These presentation changes do not introduce new ratings.

New evidence can be [submitted for review](https://github.com/BrainImagingPrivacy/BrainImagingPrivacy.github.io/issues/new?template=evidence.yml). Changes to these tables should state whether the paper itself changed or whether the website is reporting a later evidence update.
