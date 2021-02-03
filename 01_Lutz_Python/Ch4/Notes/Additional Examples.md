# Chapter Four:  Additional Examples


### Example 1:  Manually printing lines with **csv**.  Usually there will be some sort of data structure or loop that will iterate this for us.
---
```python
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
```


### Example 2:  This uses **csv** to print all of the lines using a loop.  This way, we will never try to read a line of the file that isn't there.
---
```python
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

```
