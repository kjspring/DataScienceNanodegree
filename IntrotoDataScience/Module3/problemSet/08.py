# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 19:34:28 2014

@author: kevin
"""

import numpy as np
import statsmodels.api as sm

def predictions(dataframe):
    X = dataframe[['ENTRIESn_hourly']]
    Y = dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
    Y = sm.add_constant(Y)
    model =  sm.OLS(X,Y) # make the model
    results = model.fit() # return the models
    prediction = np.dot(Y, results.params)
    return prediction

dat = predictions(turnstile_weather)