# Solutions to Additional Problems
This is just the contents of the Additional Solutions folder all on one page

## 1.) Using **csv** similar to examples 1 and 2, read data1.txt into a matrix and print it out.
---
``` python
'''
Created on Jan 31, 2021
@author: Sky Semone

Solution for question one
'''

import csv
filepath1 = 'path to data1.txt'

with open(filepath1, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i=0
    M=[]
    for row in csv_reader:
        M.append(list(row))
print(M)

```
## 2.) Using **csv**, read data2.txt into a nested list of floats.  If there is any data missing, a zero should be written.  Letting L by the nested list,
```python
>>>print(L)  

[[1.0, 101.0], [2.0, 2001.0], [3.0, 301.0], [4.0, 401.0], [5.0, 0], [6.0, 0], [7.0, 701.0]]
```
---
```python
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

```
## 3.) Again using **csv**, read data3.txt into a dictionary with the first column as the key, then with a nested list, with each row of data in the sheet as a list of floats in the dictionary  With D as the dictionary:
```python
>>>print(D['Apple'][1])  

[2.0, 2.00001]
```
---
```python
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
```
## 4.) Use **csv** to read data4.txt.  This is a data file made by a LakeShore brand VSM.  Make a nested list that contains every resistance memsurement, and the total elapsed time in seconds.  The resistance measurement can be found in the columns that start with '1' and the total time is just the running sum of the "Elapsed Time" values.  Note there are two "Elapsed Time" floats that occur for every resistance value, and it is formatted as 'hours:minutes:seconds'. 


```python
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
```
