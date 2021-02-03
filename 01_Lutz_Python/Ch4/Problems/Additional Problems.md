# Additional Questions
## 1.) Using **csv** similar to examples 1 and 2, read data1.txt into a nested list and print it out.

## 2.) Using **csv**, read data2.txt into a nested list of floats.  If there is any data missing, a zero should be written.  Letting L by the nested list,
```python
>>>print(L)  

[[1.0, 101.0], [2.0, 2001.0], [3.0, 301.0], [4.0, 401.0], [5.0, 0], [6.0, 0], [7.0, 701.0]]
```

## 3.) Again using **csv**, read data3.txt into a dictionary with the first column as the key, then with a nested list, with each row of data in the sheet as a list of floats in the dictionary  With D as the dictionary:
```python
>>>print(D['Apple'][1])  

[2.0, 2.00001]
```

## 4.) Use **csv** to read data4.txt.  This is a data file made by a LakeShore brand VSM.  Make a nested list that contains every resistance memsurement, and the total elapsed time in seconds.  The resistance measurement can be found in the columns that start with '1' and the total time is just the running sum of the "Elapsed Time" values.  Note there are two "Elapsed Time" floats that occur for every resistance value, and it is formatted as 'hours:minutes:seconds'. 
