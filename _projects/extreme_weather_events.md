---
layout: page
title: Extreme Weather Events Prediction
description: A study on ClimateNet
img: assets/img/extreme_weather_events.jpeg
importance: 2
category: ML/DL
---
## Abstract
Now more than ever, tackling climate change and minimizing the damage caused by extreme weather events is at the
forefront of humanity’s most pressing issues. As extreme climate events have and are predicted to continue becoming both
more frequent and costly (NOAA National Centers for Environmental Information 2021), having reliable
predictors of extreme climate events based on atmospherical and geographical data may be a useful tool
to both the general population and policy-makers. In this Kaggle challenge, done in the context of IFT
6390, the aim is to develop such a predictor. The challenge provides a subset of the ClimateNet dataset
(Prabhat et al. 2021) consisting of 47,760 training data points and 7,320 test data points spread over 120
locations, observed between 1996 and 2010. There are 3 distinct class labels in this subset of the data.
In the following document, we describe the preprocessing and feature selection and engineering that was done,
present the classification algorithms explored, namely multinomial logistic regression, random forest, Light Gradient
Boosted Machine (henceforth referred to as LGBM) and Extreme Gradient Boosting (henceforth referred to as XGB) and
finally discuss the evaluation methodology, results and possible future improvements.

## Report

Thumbnail source: [Wikimedia](https://commons.wikimedia.org/wiki/File:Evolution_of_a_Tornado.jpg)