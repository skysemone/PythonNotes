'''
Created on Jan 31, 2021

@author: Sky Semone

Example 1:  Using csv to import a simple file, manually read each line and print.
The last read will cause the reader to go past the bounds of the file, giving an error.
Locate 'data1.txt' for this chapter and set the correct filepath first!
'''

import csv

filepath1 = 'data1.txt'
csv_file = open(filepath1, 'r')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))

csv_file.close()
