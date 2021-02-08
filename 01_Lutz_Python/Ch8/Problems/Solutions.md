# Chaper 8 Solutions

### 1.)  Give two ways to make a list containing five integer zeros.
---
`[0,0,0,0,0]` or `[0]*5` or `([0 for i in range(5)])`

### 2.)  Give two ways to make a dictionary with values 0 for keys 'a', 'b', 'c'.
---
We can make all of the definitions at once, or append each separately, shown here:
```python
d = {'a':0,'b':0,'c':0}
#or
d = {}
d['a'] = 0
d['b'] = 0
d['c'] = 0
```

### 3.)  Name 4 operations that change a list object in place.
---
append, extend, sort, reverse, insert, remove, pop, delete

### 4.)  Name 4 operations that change a dictionary object in place.
---
del, update, d.pop(key), assigning a new key to dictionary

### 5.)  Why use a dictionary over a list?
---
Dictionaries make it easy to express labelled data, lists work best for sequential things.
