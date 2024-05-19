Title: skill issue tbh: ml time series notes 
Author: Matt Gibson
Date: 2024-04-18
Tags: statistics, machine learning, time series


Now and again I see people talking about foundation models for time series data. It's one of those things, like the puzzlement over the inability of deep learning models to outperform traditional models tabular data, that makes me think people don't grasp the generality of of tabular and time series data. Time series and tabular data are much more general than images, images and text data. In my opinion, much of the success of current methods relies on exploiting the structure of the data. The generality of these data type imho precludes finding such structure except in specific, limited cases e.g. speech recognition, weather data etc.

The M competitions have been very important in ML fore timeseries. Refs:

- [M5 accuracy competition: Results, findings, and conclusions. International Journal of Forecasting. Volume 38, Issue 4, October–December 2022, Pages 1346-1364](https://www.sciencedirect.com/science/article/pii/S0169207021001874?ref=pdf_download&fr=RR-2&rr=8794716aadbbdfc1)
- https://en.wikipedia.org/wiki/Makridakis_Competitions


Also reference data sets are available here: https://forecastingdata.org/

### trad approaches

20 Oct 2021
Do We Really Need Deep Learning Models for
Time Series Forecasting?
https://arxiv.org/pdf/2101.02118.pdf


### deep space models 

S4: deep statespace models 
https://srush.github.io/annotated-s4/


about ssm 
https://huggingface.co/blog/lbourdois/get-on-the-ssm-train

reddit post about ssm:
https://old.reddit.com/r/MachineLearning/comments/s5hajb/r_the_annotated_s4_efficiently_modeling_long/



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


### gaussian processes

- gaussian process book: https://gaussianprocess.org/gpml/chapters/RW.pdf
- Grouped Gaussian processes for solar power prediction https://link.springer.com/article/10.1007/s10994-019-05808-z

### other models - HMMs, ensembles, etc

prophet model 
THE AMERICAN STATISTICIAN
Forecasting at Scale
Sean J. Taylor and Benjamin Letham
http://lethalletham.com/ForecastingAtScale.pdf

https://github.com/facebook/prophet

https://medium.com/@cuongduong_35162/facebook-prophet-in-2023-and-beyond-c5086151c138


### frequency methods

- wavelets

### usual suspects

- lightgbm https://en.wikipedia.org/wiki/LightGBM
- xgboost https://en.wikipedia.org/wiki/XGBoost

### books
 
- Time Series Forecasting in Python  Marco Peixeiro


Python for Algorithmic Trading: From Idea to Cloud Deployment Paperback – 24 November 2020
by Yves Hilpisch (Author)
https://www.amazon.com.au/Python-Algorithmic-Trading-Cloud-Deployment/dp/149205335X/ref=srd_d_ssims_T2_d_sccl_2_5/356-5070353-2846925?pd_rd_w=Ppmna&content-id=amzn1.sym.18fa5695-611e-408b-9728-5579118370e4&pf_rd_p=18fa5695-611e-408b-9728-5579118370e4&pf_rd_r=040MT1XJP5XQ88HA3Y0A&pd_rd_wg=YwpNE&pd_rd_r=6441e172-f568-4a23-9c98-fc6e284d50ce&pd_rd_i=149205335X&psc=1

 Practical Time Series Analysis: Prediction with Statistics and Machine Learning 
https://www.amazon.com.au/Practical-Time-Analysis-Aileen-Nielsen/dp/1492041653


Modern Time Series Forecasting with Python: Explore industry-ready time series forecasting using modern machine learning and deep learning Paperback – 24 November 2022
by Manu Joseph (Author)
https://www.amazon.com.au/Modern-Time-Forecasting-Python-industry-ready/dp/1803246804/ref=pd_vtp_h_pd_vtp_h_d_sccl_3/356-5070353-2846925?pd_rd_w=SR6Mg&content-id=amzn1.sym.c3e67ad4-8c3b-4d61-8525-47091874fb48&pf_rd_p=c3e67ad4-8c3b-4d61-8525-47091874fb48&pf_rd_r=SKXN2J4TKC3MC2EMXDS8&pd_rd_wg=OQdXD&pd_rd_r=ecb8ff42-6e9d-4d73-91a2-7910d4fc26ce&pd_rd_i=1803246804&psc=1


### classical / statistics stuff 

https://otexts.com/fpp3/advanced-reading.html