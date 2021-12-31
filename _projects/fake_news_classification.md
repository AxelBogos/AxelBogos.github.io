---
layout: page
title: Fake News Classification
description: An exploration of fake news classification and the available datasets for the task
img: assets/img/fake_news_project.png
importance: 3
category: ML/DL
---

## Abstract
Accurate classification of news article as legitimate or containing fake
information has seldom been a more prominent issue. In this project, a survey
of available datasets in news classification was conducted and an evaluation of common
language models on the task of text classification was done. In addition to typical classification
models like Random Forests and XGBoost, increasingly complex language models and word embeddings such
as Word2Vec and ELECTRA were compared and used to vectorize the input and classify articles. The ELECTRA
and bi-directional LSTM models achieved the highest classification accuracy at 85%, however simpler models
also showed reasonable performances.Among our conclusions, we also draw attention to some common issues in
available datasets, some strengths and limitations of simpler word vectorization models like TFID and possible
improvements combining simpler and state-of-the-art models. 

## Repository
Available [here](https://github.com/AxelBogos/Fake-News-Classifier-Project)
## Report
<iframe src="/assets/pdf/fake_news_classification.pdf" style="width:800px; height:800px;"></iframe>

