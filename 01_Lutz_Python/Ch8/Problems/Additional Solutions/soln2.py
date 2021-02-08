'''
Created on Jan 31, 2021

@author: Sky Semone

Solution for question two
'''

import csv

filepath1 = 'path to data2.txt'

with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i=0
    L=[]
    for row in csv_reader:
        E=[]
        for d in row:
            entry = ''.join(c for c in d if  c.isdigit())
            if entry: E.append(float(entry))
            else: E.append(0)
            
        if len(E)==2:  L.append(E)
print(L)
