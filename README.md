# EPA-16s

The Impact of Weatherization on Microbial Ecology and Human Health
=================================================

## Introduction 

This repository contains scripts that have been used to analyze miRNA data.

Table of Contents 
-----------------
* [Motivation](#motivation)
* [Overview](#overview)
* [Usage](#usage)
* [Authors and history](#authors-and-history)
* [Acknowledgments](#acknowledgments)
* [References](#references)

## Motivation

Our climate is changing. The Intergovernmental Panel on Climate Change models predict mean global temperature increases of 0.2°C per decade with prolonged periods of extreme weather. These changes have the potential to influence human health through direct thermal exposure, indirect exposure to pollutants and infectious agents arising from climate change, and social and economic disruption (Parry et al., 2007). Buildings influence both climate and human health. Building weatherization initiatives attempt to mitigate climate change through energy conservation. Empirical studies suggest that air leakage accounts for up to 30% of indoor air exchange and contributes to one-third of heating and cooling energy use (Mowris and Fisk, 1988; Sherman and McWilliams, 2007). Furthermore, Spengler reports that it is possible to seal 20-40% of air leakage in existing homes and up to 90% in new construction (2010). However, while the reduction of unintentional air leakage is indeed possible and can therefore reduce a building’s contribution to climate change, the mitigation strategy may also have unanticipated human health impacts.

The role of a building is to act synergistically as an interface between climate and human health. A building is more than a third skin for thermal comfort and a second lung for respiration; it is also a second microbiome for immunity. Our understanding of what constitutes a healthy building now includes a new metric for defining it: microbial community diversity. The loss of microbial diversity is increasingly becoming understood as correlated with negative health outcomes (von Hertzen et al., 2011; Cho and Blaser, 2012; Johnson, 2013). Human immune function, having evolved within a highly diverse microbial environment, is biased towards a diversity of microbial challenge. Sufficient stimulation of the immune system releases cytokines that regulate the central nervous system; however, insufficient microbial challenge results in an over-reactive immunity that can induce chronic inflammatory disorders such as atopy and asthma, autoimmune dysfunctions such as psoriasis and rheumatoid arthritis, cardiovascular disease, diabetes mellitus, cancer and neuropsychiatric conditions (Russell et al., 2012; Ege et al., 2012; Rook et al., 2013). 

We are beginning to move from a paradigm that considers all microbes "bad" and potentially pathogenic toward a new understanding of the role of microbial communities in promoting positive health (Sachs, 2007). Recent research suggests there are in fact potentially negative impacts to immune system development deriving from a lack of exposure to environmental microbial diversity (Rook, 2010) and that environmental factors may have the greatest health impact during childhood (Russell et al., 2012). Several studies have found that exposure to a diversity of soil, plant and animal microbes may be beneficial or even necessary for proper immune development and regulation. For example, Hanski et al. (2012) found positive correlations between exposure to highly vegetated environments and skin microbiota diversity, both of which were associated with a lower likelihood of allergic disposition. Ege et al. (2011) compared children living on farms with those in a reference group and linked exposure to higher microbial diversity with a lower prevalence of asthma and allergic sensitivity. Shu et al. (2013) found commensal bacteria of the skin microbiome to be protective against colonization of methicillin-resistant Staphylococcus aureus. These empirical studies are supported by theoretical work seeking to elucidate the physical mechanisms through which the protective effects of diverse microbial exposure might occur (Eder et al., 2006; Heederik and von Mutius, 2012; Rook et al., 2013; Raison et al., 2010; Raison and Miller, 2013; von Hertzen et al., 2011).

Although humans spend 90% of their time indoors, only recently has the scientific community begun to explore the abundance, diversity and biogeography of microbiota in buildings using nonculture-based techniques (Kembel et al., 2012; Meadow et al., 2013; Adams et al., 2013; Hewitt et al., 2012; Kembel et al., 2014). The burgeoning understanding of this unexplored habitat highlights the role ventilation plays in structuring the indoor microbiome (Meadow et al., 2013). Direct ventilation at the building envelope has been shown to increase indoor microbial diversity and abundance of outdoor commensal microbes, while filtered mechanical ventilation results in decreased microbial diversity and a preponderance of human-associated microbes and potential pathogens in indoor air (Kembel et al., 2012). Indoor microbial communities closely track outdoor sources; however the building enclosure may act as a selective filter, depending on the ventilation design, attenuating beneficial outdoor-associated microbes and concentrating human-associated microbes, including pathogens, such as multi-drug resistant Staphylococcus aureus (MRSA) (Kembel et al., 2012; Meadow et al., 2013; Gandara et al., 2006). The complex interplay of microbial shifts, climate variability, human and vector migrations and emerging infectious disease outbreaks is dynamic and cannot be predicted for its net health effect (Lach et al., 2010). However, the indirect result of climate change initiatives such as weatherization programs and low-rise residential ventilation recommendations (such as based on ASHRAE 62.2-2013) could further diminish microbial diversity in the built environment indoor ecology.

Low-rise residential buildings typically ventilate by wind or temperature driven pressure differentials through windows and cracks in the building envelope (Figure 1) and intermittent occupant-controlled exhaust fans. Weatherization reduces the un-designed air inlets by sealing the envelope. Studies have demonstrated increases in indoor air contaminants such as VOC’s, formaldehyde and CO2 in tightly-sealed homes and have shown whole house mechanical ventilation systems to be effective in reducing the concentration of these contaminants. ASHRAE 62.2-2013 addresses the effect of a less porous building envelope and the corresponding concentration of indoor air contaminants by specifying three mechanical systems for whole house continuous ventilation (Figure 2). This guideline does not address energy use, and may have implications for indoor ecology. The distributed inlet mechanical model is being used as a proxy for designed natural ventilation, which can achieve the same result with less energy use and more robustness against power outages associated with climate change. Unlike commercial buildings, design generally follows prescriptive code paths and is unlikely to be influenced by engineers, architects or building scientists once codified; therefore, addressing the science determining building code has the potential for widespread national impact. We will investigate homes with these systems in diverse climate zones (marine and high desert) to compare their effect on indoor microbiota based on the source of ventilation, localized (ducted) or distributed (envelope-associated), using ASHRAE 62.2-2013 prescribed ventilation rates.  


## Overview
We set out to study the ways that weatherization alters indoor air quality, including the composition and structure of indoor microbial communities. We sampled microorganisms, a wide range of air quality metrics, and administered an extensive health and behavior survey in 66 homes across Portland, OR. While we observed no gross effect of weatherization treatment, we found that the community dissimilarity between paired indoor/outdoor bioaerosol samples is related to seasonal patterns of window operation, and that the synchrony between indoor/outdoor air quality measures helps explain the dissimilarity in microbial communities. This helps us understand the relationship between home operation and shifts in microbial community dynamics that may affect the health of building occupants. 

![cover](./weatherized.png)

## Usage
- Clone the repository
```bash
git clone 'https://github.com/beagan-svg/EPA-16s'
```
- Navigate to each subdirectory and execute its readme 

## Authors and History

* Beagan Nguy - Algorithm Design

## Acknowledgments

We’d like to thank the BIOBE Team
 
## References 
- [1] Kembel SW, Jones E, Kline J, Northcutt D, Stenson J, Womack AM et al. 2012. ISME 6:1469–1479.
- [2] Lax S, Smith DP, Hampton-Marcell J, Owens SM, Handley KM, Scott NM, et al. 2014. Science 345:1048–1052.
- [3] Meadow JF, Altrichter AE, Kembel SW, Kline J, Mhuireach G, Moriyama M, et al. 2014. Indoor Air 24:41–48.
- [4] NASEM. 2017. Microbiomes of the Built Environment. Washington, DC: The National Academies Press.
Pigg S, Cautley D, Francisco PW. 2017. Indoor Air.
- [5] Vandegrift, R. et al. “Seasonality and window operation drive indoor microbial ecology”.
Manuscript in preparation.
- [6] Ishaq, S.L. et al. “Microscopic roommates: The biological sources of indoor air bacteria of
single - family homes in Portland, Oregon.” Manuscript in preparation.
- [7] Cil, G. et al. “Health measures following home weatherization in single - family homes in Portland, Oregon.” Manuscript in preparation.
- [8] Vandegrift, R. et al. “Shut the front door: seasonal patterns in window operation drive fungal and bacterial community dissimilarity between indoor and outdoor air.” 15th Conference of the International Society of Indoor Air Quality and Climate (ISIAQ). Philadelphia, PA. July 2018. 
