# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 10:49:16 2014

@author: kevin
"""

import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        filein = name
        fileout = open('updated_' + name, 'w+')
        
        with open(filein, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                for group in range(0, (len(row) - 3)//5):
                    record = row[0:3] + row[3+5*group:8+5*group]
                    fileout.write(','.join(record) + '\n')
                    
        f.close()
        fileout.close()