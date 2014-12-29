# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 10:59:37 2014

@author: kevin
"""

def format_key(fog, rain):
    return '{}fog-{}rain'.format(
        '' if fog else 'no',
        '' if rain else 'no'
    )
    
f = open('turnstile_data_master_with_weather.csv')
lines = f.readlines()
f.close()
data = lines[13910].strip().split(",")