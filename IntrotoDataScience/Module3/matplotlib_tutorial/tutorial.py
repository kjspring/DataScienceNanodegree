# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 11:56:14 2014

@author: kevin
"""
# Data structures

import numpy as np

randn = np.random.randn
from pandas import *

'''Series is a one-dimentional labeled array capable of holding any data type.
the axis labels are referred to as the index.
'''

s = Series(randn(5), index=['a', 'b', 'c', 'd', 'e'])

# from dict
d = {'a':0., 'b': 1., 'c':2.}
print Series(d, index=['b', 'c', 'd', 'a'])

# Dataframe
'''A 2-dimentional labeled data structure with columns of potentially
different types. Most commonly used pandas object.
'''
d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
