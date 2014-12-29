# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 18:42:30 2014

@author: kevin
"""

import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv


    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) != 12 or data[0] == 'Registrar':
            #logging.info("%s, has been skipped", data)
            continue
        print "{0}\t{1}".format(data[3], data[8])
        #logging.info(data[3], data[8])
        
def reducer():
    aadhaar_generated = 0
    old_key = None
    
    for line in sys.stdin:
        data = line.strip().split("\t")
        #logging.info(data)
        
        if len(data) != 2:
            continue #next row
        
        this_key, count = data
        #logging.info(this_key)
        
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key, aadhaar_generated)
            #logging.info("{0}\t{1}".format(old_key, aadhaar_generated))
            aadhaar_generated = 0
        
        old_key = this_key
        aadhaar_generated += float(count)
    
    if old_key != None:
        print "{0}\t{1}".format(old_key, aadhaar_generated)
        #logging.info("{0}\t{1}".format(old_key, aadhaar_generated))

mapper()
