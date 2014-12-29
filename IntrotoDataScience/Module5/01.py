# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 17:35:21 2014

@author: kevin
"""

#import logging
import sys
import string

dat_input = 'Hello my name is Kevin!'

def word_count(dat_input):
    word_counts = {}
   
    for line in sys.stdin:
        data = line.strip().split(" ")

        for i in data:
            key = i.translate(string.maketrans("", ""), string.punctuation).lower()
            if key in word_counts.keys():
                word_counts[key] += 1
            else:
                word_counts[key] = 1
    print word_counts

word_count(dat_input)
