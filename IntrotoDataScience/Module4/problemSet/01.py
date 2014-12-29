# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 13:38:26 2014

@author: kevin
"""

import pandas
from ggplot import *

os.chdir('/home/kevin/Dropbox/courses/Udacity/DataScience/IntrotoDataScience/Module4/problemSet')

turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    plot = ggplot(turnstile_weather, aes('Hour', 'ENTRIESn_hourly', color= 'UNIT')) + geom_jitter()
    return plot

def plot_hist(dat, rain_type):
    #dat_sub = dat[dat.rain == r_type]
    plot = ggplot(dat, aes(x='ENTRIESn_hourly')) 
    plot = plot + geom_histogram()
    plot = plot + xlab('entries') + ylab('frequency')
    plot = plot + ggtitle('Histogram of ' + rain_type + ' days')
    return plot

def plot_rainvsnorain(dat):
    plot = ggplot(dat, aes(x='rain', y='ENTRIESn_hourly'))
    #plot = plot + geom_bar(stat = 'identity', colour = 'black')
    #plot = 
    return plot
    
#print plot_weather_data(turnstile_weather)

#print plot_hist(turnstile_weather, 'rain')

rainy_weather.index = range(rainy_weather.shape[0])
rainy_weather = turnstile_weather[(turnstile_weather['rain'] == 1)]
print plot_hist(rainy_weather, 'rainy')

#print plot_rainvsnorain(turnstile_weather)