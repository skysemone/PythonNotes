# Chaper 9 Solutions

### 1.)  How do you determine the size of a tuple?
---
`len()`

### 2.)  Write an expression that changes the first term in a tuple; i.e. (1,2,3) -> (0,2,3)
---
Again, tuples are immutable, so we have to do something like...
```python
t=(1,2,3)
t=(1,)+t[1:]
```

### 3.)  What is the default for the processing mode argument in a file `open` call?
---
The default is 'r' for reading.

### 4.)  What module stores Python objects in a file without converting them to strings yourself?
---
The 'pickle' module.

### 5.)  How can you copy all parts of a nested structure?
---
Import 'copy' and call `copy.deepcopy(x)`.

### 6.)  When does Python consider an object `True`?
---
If its a non-zero number or a non-empty collection

### 7.)  "What is your quest"
---
insert Monty Python joke here (sigh)
