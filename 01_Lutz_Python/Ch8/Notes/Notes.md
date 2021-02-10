# Chapter Eight:  Lists and Dictionaries


## Lists
Lists have the following properties:
+ **Mutable sequences** 
+ **Ordered collections of arbitrary objects:** any object can be placed in a list
+ **Accessed by index:**  objects are ordered by index position 
+ **Variable-length, heterogeneous, and arbitratily nestable:** Lists can grow in place unlike strings.  Objects can be added, removed, and nested.
+ **Arrays of reference objects:**  Once a list is made, any variable associated to it will be able to edit the list object.

### Basic operations for lists
| Method |  |
|-|-|
|append()  |  Adds an element at the end of the list|
|clear()  |  Removes all the elements from the list|
|copy()  |  Returns a copy of the list|
|count()  |  Returns the number of elements with the specified value|
|extend()  |  Add the elements of a list (or any iterable), to the end of the current list|
|index() |   Returns the index of the first element with the specified value|
|insert()   | Adds an element at the specified position|
|pop()  |  Removes the element at the specified position|
|remove()  |  Removes the first item with the specified value|
|reverse()  |  Reverses the order of the list|
|sort()   | Sorts the list|




## Intro to Lists
### Basic operations
Here are some basic examples of using lists
```python
a = [1,2,3]
b = [4,5,6]
print(a+b)      #[1, 2, 3, 4, 5, 6]
a.append(b)
print(a)        #[1, 2, 3, [4, 5, 6]]
b.append('b')
print(a)        #[1, 2, 3, [4, 5, 6, 'b']]
```


```python
a = [[1,2,3],[4,5,6],[7,8,9]]
print(a[1][2])
```

### Comprehensions
To test the membership if a list:
```python
a = 3 in [1,2,3,4]      #prints true
```
To iterate through a list:
```python
a = [1,2,3,4]
for x in a:
    print(x)
```
With these tools, we can construct our first list sequence:
```python
a = [c*4 for c in 'test']
print(a)
```
### Indexing, slicing, matricies
Indicies for lists behave like string indicies, except lists can be nested, allowing for multiple indicies (this can get confusing for more than 2 indicies sometimes.)
```python
a =  [[1,2,3],
[4,5,6],
[7,8,9]]
b = [[[1,2,3],[4,5,6],[7,8,9]],  [[10,11,12],[13,14,15],[16,17,18]]]
print(a[1][2], b[1][2])
```

### Changing lists in place
This can be done since lists are not mutable
```python
a = [1,2,3]
a[0] = 'test'
print(a)
```
To delete part of a list, we can just insert nothing over a range
```python
a = [1,2,3]
a[0:1] = []
print(a)
```


### Sorting lists
For the following examples, a list will be made using both upper and lowercase strings.  By changing the arguments in the `sort()` method, we can achieve many different ways to sort our data.  This can also be helpful for the dictionaries discussed later in this chaper.
```python
a = ['abc','abe', 'ABC', 'ABE']
a.sort()
print(a)                        #['ABC', 'ABE', 'abc', 'abe']

#   normalize to lowercase
a.sort(key=str.lower)
print(a)                        #['ABC', 'abc', 'ABE', 'abe']

#   reverse sort order
a.sort(key=str.lower, reverse=True)
print(a)                        #['ABE', 'abe', 'ABC', 'abc']

#   notice that when the method is called in the print statement, the return type is None, so "None" is printed
print(a.sort())                 # None
```

More examples of using methods here.  The extends method adds the contents of its argument to the end of the list.  Notice that this is different than concatenation, which would place the whole argument as one entry at the end of the list.  Pop will take the last element of the list (or object called by index argument) and return that object.  The list will have that object removed as a result.  Reverse just reverses the list.
```python

a = [1,2,3]
a.extend(['a','b','c'])
print(a)                        #[1, 2, 3, 'a', 'b', 'c']

a.pop()     
print(a)                        #[1, 2, 3, 'a', 'b']
a.pop(1)
print(a.pop(0))                 #1
print(a)                        #[3, 'a', 'b']

a.reverse()
print(a)                        #['b', 'a', 3]
```






## Dictionaries
