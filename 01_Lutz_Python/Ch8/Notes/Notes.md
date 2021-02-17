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
Dictionaries have the following properties:
+ **Accessed by key, not offset position (index):**  to retrieve an object from a dictionary, a key must be used.  Objects are entered into the dictionary with this key.
+ **Unordered collections of arbitrary objects:**  There is to index value for the object
+ **Variable-length, heterogeneous, and arbitrarily nestable:**  Dictionaries can grow in place unlike immutable objects.  Objects can be added, removed, and nested.
+ **Mutable mapping:**  dictionaries can be changed in place
+ **Table of reference objects:**  it is a hash table, therefore implemented to be fast.

### Basic operations and methods for dictionaries
| Operation |  |
|-|-|
| keys() | returns all keys in form dict_keys(['a', 'b', 'c']) |
| values() | returns all values in form dict_values([1, 2, 3]) |
| items() | returns al objects similarly |
| copy() | top-level copy |
| clear() | removes all objects  |
| update(d2) | merges dictionaries |
| get(key) | returns object by key |
| pop(key) | returns object and removed from dictionary | 
| len(d) | number of stored entry |

### Using dictionaries

To make a dictionary, code something like this.  I will use this dictionary in most of the examples
```python
d = {'a':1,'b':2,'c':3,'d':4}

```
Now we can change and add things to the dictionary:
```python
d = {'a':1,'b':2,'c':3,'d':4}
#   change an object
d['a'] = 10
print(d)

#   delete an object
del d['a']
print(d)

```

These methods allow us to view objects in the dictionary:

```python
d = {'a':1,'b':2,'c':3,'d':4}
#   show values/keys in a list
print(list(d.values()))
print(list(d.keys()))

#   retrieve a value
item = d.get('b')
print(item)

#   notice that the get method will return None if object not present
item = d.get('nope')
print(item)

```
`update()` and `pop()` work just like they do for lists.

### An example database using dictionaries
```python
table = {'1975': 'Holy Grail',
         '1979': 'Life of Brian',
         '1983': 'The Meaning of Life'
}
year  = '1983'
movie = table[year]

#print the title of the movie for this year
print(movie)

#print out all of the data we have
for year in table:
    print(year + '\t' + table[year])
```

### Notes on how to use a dictionary

The book mentions the next three points when working with dictionaries
1. You can't do sequential operations since there are no indicies
2. Assigning to new indicies adds entries
3. Keys can be any immutable object


Missing key errors occur when we try to look up something that is not contained in our dictionary.  These will look something like this:

```python
Traceback (most recent call last):
  File "/Users/skysemone/Documents/python review/test project/q6.py", line 22, in <module>
    a['test']    
KeyError: 'test'
```
where 'test' is the name of the string I tried to look up.  The book giving the following ways to avoid this error and just return nothing without crashing the program. I will use the 'table' dictionary in the previous example
```python
a = '1990'

#   option 1:  if it exists then do something
if a in table:
    print(table[a])
else:
    print(0)

#   option 2:  catch the error
try:
    print(table[a])
except KeyError:
    print(0)
    
#   option 3:  the default value is 0, if the object isnt found 0 will be printed
table.get(a,0)
```
