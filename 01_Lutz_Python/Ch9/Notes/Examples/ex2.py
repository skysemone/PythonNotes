'''
Created on Jan 31, 2021

@author: Sky Semone

Example 1:  Using csv to import a simple file, manually read each line and print.
This does nearly the same as example 1, but is much more sleek and does not run
past the end of the file!
'''

import csv

filepath1 = 'data1.txt'

with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
