'''
Created on Jan 31, 2021
@author: Sky Semone

Solution for question one
'''

import csv
filepath1 = 'data1.txt'

with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i=0
    M=[]
    for row in csv_reader:
        M.append(list(row))
print(M)
