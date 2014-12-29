# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 11:10:40 2014

@author: kevin
"""

import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    """
    The input to this mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise.  You can check out the csv and its structure below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    For each line of input, the mapper output should PRINT (not return) the UNIT as 
    the key, the number of ENTRIESn_hourly as the value, and separate the key and 
    the value by a tab. For example: 'R002\t105105.0'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    
    The logging module can be used to give you more control over your debugging
    or other messages than you can get by printing them. In this exercise, print
    statements from your mapper will go to your reducer, and print statements
    from your reducer will be considered your final output. By contrast, messages
    logged via the loggers we configured will be saved to two files, one
    for the mapper and one for the reducer. If you click "Test Run", then we
    will show the contents of those files once your program has finished running.
    The logging module also has other capabilities; see 
    https://docs.python.org/2/library/logging.html for more information.
    """

    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) == 22 and data[6] == "ENTRIESn_hourly":
            continue
        print "{0}\t{1}".format(data[1], float(data[6]))
        logging.info(data[1], data[6])


mapper()

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''
    riders = 0 # number of riders
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
            print "{0}\t{1}".format(old_key, riders)
            logging.info("{0}\t{1}".format(old_key, riders))
            riders = 0
            
        old_key = this_key
        riders += float(count)
        
    if old_key != None:
        print "{0}\t{1}".format(old_key, riders)
        logging.info("{0}\t{1}".format(old_key, riders))
        
reducer()

