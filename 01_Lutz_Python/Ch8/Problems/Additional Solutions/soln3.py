'''
Created on Jan 31, 2021

@author: Sky Semone

Solution for question three
'''

import csv

filepath1 = 'path to data3.txt'

D={}
F=[]
with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for row in csv_reader:
        if len(row)==1:
            fruitName = row[0]
            D[fruitName] = F
            F=[]
        else:
            E=[]
            for d in row:
                if d: E.append(float(d))
            F.append(E)
        D[fruitName] = F
       
print(D['Apple'][1])
