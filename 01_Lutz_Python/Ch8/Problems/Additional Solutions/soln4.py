'''
Created on Jan 31, 2021

@author: Sky Semone

Solution for question three
'''

import csv

filepath1 = 'path to data4.txt'

F=[['resistance', 'total time']]
totalTime = 0
with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for row in csv_reader:
        if row:
            if row[0]=='Elapsed Time:':
                timeList = row[1].split(':')
                
                totalTime += 3600*float(timeList[0])+60*float(timeList[1])\
                + float(timeList[2])

            if row[0]=='1':
                F.append([float(row[1]), totalTime])
                print(row)

print(F)
