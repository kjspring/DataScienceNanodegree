# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 19:07:22 2014

@author: kevin
"""

import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    '''
    For this exercise, compute the average value of the ENTRIESn_hourly column 
    for different weather types. Weather type will be defined based on the 
    combination of the columns fog and rain (which are boolean values).
    For example, one output of our reducer would be the average hourly entries 
    across all hours when it was raining but not foggy.

    Each line of input will be a row from our final Subway-MTA dataset in csv format.
    You can check out the input csv file and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    
    Note that this is a comma-separated file.

    This mapper should PRINT (not return) the weather type as the key (use the 
    given helper function to format the weather type correctly) and the number in 
    the ENTRIESn_hourly column as the value. They should be separated by a tab.
    For example: 'fog-norain\t12345'
    
    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    # Takes in variables indicating whether it is foggy and/or rainy and
    # returns a formatted key that you should output.  The variables passed in
    # can be booleans, ints (0 for false and 1 for true) or floats (0.0 for
    # false and 1.0 for true), but the strings '0.0' and '1.0' will not work,
    # so make sure you convert these values to an appropriate type before
    # calling the function.
    def format_key(fog, rain):
        return '{}fog-{}rain'.format(
            '' if fog else 'no',
            '' if rain else 'no'
        )

    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 22 and data[6] == "ENTRIESn_hourly":
            logging.info("%s, has been skipped", data)
            continue
        weather = format_key(float(data[14]), float(data[15]))
        print "{0}\t{1}".format(weather, float(data[6]))
        logging.info(weather, data[6])
     

mapper()

def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable 
    riders and num_hours below. Feel free to use a different data structure in 
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t") # split the input on the tab
        logging.info(data)
        
        if len(data) != 2: # gets rid of invalid key:value pairs
            logging.info("%s, has been skipped", data)
            continue # next row
            
        this_key, count = data # store the current key and the count
        logging.info(this_key)
        
        if old_key and old_key != this_key: # if there is an old_key and it is dif from the currnt key
            print "{0}\t{1}".format(old_key, riders/num_hours)
            logging.info("{0}\t{1}".format(old_key, riders))
            riders = 0
            num_hours = 0
            
        old_key = this_key
        riders += float(count)
        num_hours += 1
        
    if old_key != None:
        print "{0}\t{1}".format(old_key, riders)
        logging.info("{0}\t{1}".format(old_key, riders/num_hours))

reducer()