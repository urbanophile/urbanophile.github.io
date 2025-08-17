Title: skill issue tbh: ml time series notes 
Author: Matt Gibson
Date: 2024-04-18
Tags: statistics, machine learning, time series
Modified: 2025-01-07


Now and again I see people talking about foundation models for time series data. It's one of those things, like the puzzlement over the inability of deep learning models to outperform traditional models tabular data, that makes me think people don't grasp the generality of of tabular and time series data. Time series and tabular data are much more general than images, images and text data. In my opinion, much of the success of current methods relies on exploiting the structure of the data. The generality of these data type imho precludes finding such structure except in specific, limited cases e.g. speech recognition, weather data etc.

The M competitions have been very important in ML fore timeseries. Refs:

- [M5 accuracy competition: Results, findings, and conclusions. International Journal of Forecasting. Volume 38, Issue 4, October–December 2022, Pages 1346-1364](https://www.sciencedirect.com/science/article/pii/S0169207021001874?ref=pdf_download&fr=RR-2&rr=8794716aadbbdfc1)
- https://en.wikipedia.org/wiki/Makridakis_Competitions


Also reference data sets for the competitions M* are [available here](https://forecastingdata.org/).

## Approaches

### usual suspects

- lightgbm https://en.wikipedia.org/wiki/LightGBM
- xgboost https://en.wikipedia.org/wiki/XGBoost

A classical approach for time series modelling in machine learning is Gaussian Processes:

- The canonical reference is [gaussian process book](https://gaussianprocess.org/gpml/chapters/RW.pdf)
- An interesting application to solar energy is [Grouped Gaussian processes for solar power prediction](https://link.springer.com/article/10.1007/s10994-019-05808-z)

#### frequency methods

- wavelets

#### other models - HMMs, ensembles, etc

An interesting and somewhat controversial topic is the "self-tuning" prophet models developed by Facebook researchers Sean Taylor and Benjamin Lentham. 

- [paper](http://lethalletham.com/ForecastingAtScale.pdf)  Forecasting at Scale. THE AMERICAN STATISTICIAN Sean J. Taylor and Benjamin Letham
- [github](https://github.com/facebook/prophet)
- EOL for prophet package [blog post](https://medium.com/@cuongduong_35162/facebook-prophet-in-2023-and-beyond-c5086151c138)
- [a seed of the controversy](https://ryxcommar.com/2021/11/06/zillow-prophet-time-series-and-prices/)

### neural net approaches

A Survey of Deep Learning and Foundation Models for Time
Series Forecasting
JOHN A. MILLER, MOHAMMED ALDOSARI, FARAH SAEED, NASID HABIB BARNA,
SUBAS RANA, I. BUDAK ARPINAR, and NINGHAO LIU
5 Jan 2024
https://arxiv.org/pdf/2401.13912.pdf

with tensorflow:
https://www.tensorflow.org/tutorials/structured_data/time_series


N-BEATS: Time-Series Forecasting with Neural Basis Expansion
https://nixtlaverse.nixtla.io/neuralforecast/models.nbeats.html

"TimeGPT"
https://arxiv.org/abs/2310.03589


resurrecting recurrent neural networks for long squences
https://openreview.net/pdf?id=M3Yd3QyRG4


#### deep space models 

20 Oct 2021
Do We Really Need Deep Learning Models for
Time Series Forecasting?
https://arxiv.org/pdf/2101.02118.pdf


S4: deep statespace models 
https://srush.github.io/annotated-s4/


about ssm 
https://huggingface.co/blog/lbourdois/get-on-the-ssm-train

reddit post about ssm:
https://old.reddit.com/r/MachineLearning/comments/s5hajb/r_the_annotated_s4_efficiently_modeling_long/





## Reference material

### Books
Time series arise in so many application the literature about them is enormous, but  the resources here are practically focused.

- A very useful book for learning basic time series is by Robert Hyndman and co called ["Forecasting: Principles and Practice"](https://otexts.com/fpp3/advanced-reading.html)
- Any econometrics textbook will have a discussion of time series methods and/or it's cousin, panel data. 
- [Time Series Forecasting in Python] by Marco Peixeiro
- [Python for Algorithmic Trading (2020) Yves Hilpisch](https://www.amazon.com.au/Python-Algorithmic-Trading-Cloud-Deployment/dp/149205335X/)
- [Practical Time Series Analysis: Prediction with Statistics and Machine Learning](https://www.amazon.com.au/Practical-Time-Analysis-Aileen-Nielsen/dp/1492041653)
- [Modern Time Series Forecasting with Python (2022) Manu Joseph](https://www.amazon.com.au/Modern-Time-Forecasting-Python-industry-ready/dp/1803246804/)

### Libraries