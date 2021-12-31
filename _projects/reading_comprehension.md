---
layout: page
title: Reading Understanding with transformers
description: A SemEval-2021 reading comprehension task approached with Transformers
img: assets/img/transformer.gif
importance: 3
category: ML/DL
---
This project consisted of a task from the SemEval 2021 workshop. SemEval is an international shared task on semantic
evaluation organized by the Special Interest Group on the Lexicon of the Association for Computational Linguistics1.
The task chosen is the task four of the 2021 workshop: Reading Comprehension of Abstract Meaning. 
This task consisted of bench-marking the reading comprehension capabilities of current models.
The means by which this capability is measured is by predicting a missing word from a summary of a given text from a
list of choices. That is, the input consists of a text, a summary where a particular word is removed and 5 options
for the word that best represents the meaning of the text. A example is shown in table 1. The task is subdivided in
three closely related sub-tasks: sub-task 1 requires the model to perform reading comprehension bench-marking as
previously described where the missing word represent imperceptible concepts, such as objective, culture or economy.
The example shown in table 1 belongs to this sub-task. sub-task 2 is concerned with reading comprehension where the
missing word is a concrete object, like groundhog, or chair. Sub-task 3 evaluates the performance of a model trained
on one of the sub-task and tested on the other, for instance a model trained to perform reading comprehension on
imperceptible concepts and tested on text passages where the missing word is a concrete entity. Hence the difference
in the sub-tasks lies mainly in the data used to train and evaluate the model.

## Report
<iframe src="/assets/pdf/reading_comprehension.pdf" style="width:800px; height:800px;"></iframe>

Thumbnail source: [Jay Alammar's illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)