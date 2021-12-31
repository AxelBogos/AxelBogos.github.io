---
layout: post
title:  Hospitalizations and Cases by Vaccine Status
date: 2021-12-30 19:32:00
description: A visualization of the differences in hospitalizations and case incidence rates as a function of vaccine status
tags: covid visualizations
categories: personal-posts
---
## Motivation
Despite some great visualizations being available for all things COVID ([Radio-Canada in Canada](https://ici.radio-canada.ca/info/2020/coronavirus-covid-19-pandemie-cas-carte-maladie-symptomes-propagation/)
and [Our World in Data worldwide](https://ourworldindata.org/coronavirus) to name but two), I have yet to find a single-source visualization of 
the difference in impact of the current omnicron wave across vaccinated and unvaccinated groups.

## Visualization
<iframe width="1000" height="750" frameborder="0" scrolling="yes" src="/assets/figures/Hosps_and_cases_vs_vacc_rate.html"></iframe>

## Sources
Hospitalization & Cases Data:  [Données Québec](https://www.donneesquebec.ca/recherche/dataset/covid-19-portrait-quotidien-des-cas-confirmes)
<br>
Vaccination Status Data: [Institut national de
santé publique du Québec](https://www.inspq.qc.ca/covid-19/donnees/vaccination) (Figure 2.1 of the link)

## Code
You can check out the Jupyter Notebook [here](https://drive.google.com/file/d/1A98XA_otgyHjx9yVocbuZVFuTSZ8fOtH/view?usp=sharing). 
The project will be published as a repository soon.

## Future Developments
 * Add a slider to control the moving average period
 * Expand the visualization to other provinces/countries.

