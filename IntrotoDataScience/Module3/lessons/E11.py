# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 10:54:37 2014

@author: kevin
"""

import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.
    r_squared = 1 - (np.subtract(predictions, data)**2).sum() / (np.subtract(data, data.mean())**2).sum()

    return r_squared