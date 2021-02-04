# Chapter Five:  Numeric Types

## Basics



This book presents numeric data types before strings, lists etc since numbers are so fundamental to structuring and expressing objects in Python.  While the book goes into great detail explaining the underlying mathematics, I will assume a basic understanding of discrete mathematics to direct this section of notes toward application.

Many of the mathematical hammers used in Python need to be imported from numpy and other modules; these are consequentially excluded from most of the book and these set of notes.  The built in functions and modules for mathematical objects in Python include:
 + round
 + math
 + random
 
 
## Types of Numbers

+ Integers
+ Hex, Octal, Binary literals
+ Complex 
+ Fractions


## Differences Between Python2 and Python3

| Expression | Python 2 | Python 3|
| ------ | ----------- | ---------- |
| `10/4`  | 2 | 2.5 |
| `10/4.0` | 2.5| 2.5 |
| `10//4`    | 2 | 2 |
|`10//4.0`  | 2.0 | 2.0 |




+ Functional:  programs are constructed by applying and composing functions.  Functions in this sense are based on the mathematical functions, which takes an input and maps it to a single output.  Languages like LISP and Haskell, while there has been a trend to include



 + Functional:  programs are constructed by applying and composing functions.  Functions in this sense are based on the mathematical functions, which takes an input and maps it to a single output.  Languages like LISP and Haskell, while there has been a trend to include functional elements in newer programming languages liek C#.  Today even Java and Fortran have functional elements.
 + Imperitive: uses instructions to change the state of the program.  Think of this as telling the computer step by step what to do.  There are many variants of this, but the most are considered procedural (having subroutines/functions.)
 + Structured:  Similar to imparitive languages, these are langauges that give instructions, but impove claity and efficiency by using several control flow methods like while loops, for loops, if statements, etc. 
 + Reflexive:  programming languages able to examinge, introspect, and modify its own structure.

 
## Built in Types

In lower level languages, programmers have to code (or copy) their own data structures, but python has many objects and data structures already defined and optimized.  additionally, python makes importing external libraries and packages very easy with PIP (Package installer for Python.)

Here are examples of many of the types to be covered in this section:

``` python
    #<class 'int'>    
    x = 123
    print(type(x))

    #<class 'float'>
    x = 123.0
    print(type(x))

    #<class 'float'>  multiplying int and float
    x = 123.0
    y = 4
    print(type(x*y))

    #<class 'complex'>
    x = '12+3j'
    print(type(x))

    #<class 'bool'>
    x = 123==321
    print(type(x))

    #<class 'str'>
    x = '123.0'
    print(type(x))

    #<class 'tuple'>
    x = (123.0,123,123)
    print(type(x))

    #<class 'list'>
    x=[1,2,3,4,5]
    print(type(x))

    #<class 'set'>
    x={1,2,3,4,5}
    print(type(x))

    #<class 'dict'>
    x={1:'entry 1', 2:'entry 2', 'c': 'entry c'}
    print(type(x))
``` 



## Strings

Strings can be used to record names, words, and other textual information, but it can also be used to store other collections of data.  In either case, the most frequent operations on strings involving copying the string, separating it into smaller sub-strings, or conbining strings together.  Strings start at position '0' and continue to the position of the last letter in the defined string.

### Immutability and Object ID
Strings are immutable in python as they are in many other languages.  This means that when a string in defined in memory, making any change to the string with code will not just make a similar change in the memory, but copy the string to a new position of memory with the changes made.  Lets say that we have string **a='Immutable'**, and we wanted to add an **'s'** to the end.  **c=a+'s'** will result in the new string **'Immutables'**.  The consequences of this will be highlighted in the follwing examples

The fastest way to show this is by trying to change a letter in a string
``` python
a='test'__
a[0]='b'  
#   TypeError: 'str' object does not support item assignment
```

but you can do something like this in a list:

``` python
a=['t', 'e','s','t']
a[0]='b'
print(a)
```
 
 What you can do is select part of the string and add it to another part:
 ``` python
a='test'
b='b'+a[1:]
print(b)
#   'best'
```
 
 This is a good place to bring up '==' and 'is' in Python.  Every object defined in the Python code gets a unique ID upon creation.  In CPython this is the memory address, but using the standard implimentation, it is a constant value.  'is' should be used to check identity, and '==' used to check equalivance.  Using 'is' to compare two strings, in this case, is the equilivant to this statement using '=='

 **id(a)==id(b)**    <=>   **a is b**
 
 Python caches strings and objects to minimize space, so two different strings will still show up as the same id, while strings constructed through other means will not.
 ``` python
a='string 1'
b='string 1'
print(id(a), id(b))
#    4385830064 4385830064

a='string 1'
b=a[0:2]+a[2:5]
print(id(a), id(b))
#   4372340336 4372236592
```
so in this instance, **'a==b'** returns true, but **'a is b'** returns false.
 

### Using Regular Expressions for Strings
This section will use resources outside of the Lutz text.
#### What are regular expressions
#### Special characters
These characters will match:
+ **.**   any given character except the newline (DOTALL flag overrides this exception.
+  **^**  the start of a string (and after newlines if in MULTILINE mode)
+  **$**  the end of a string (and before a newline in MULTILINE mode)
+ **\*** 0 or more repetitions of the proceeding RE
+  **+**  1 or more repetitions of the proceeding RE+
+ **?**  0 or 1 repetitions of the proceeding RE
+ **_?** adding '?' after the qualifier match as few character as possible
+ **{m}** m copies of previous RE
+ **{m,n}** m to n copies of previous RE
+ **[]** a set of characters
+ **a|b** set a or set b
+ **\w** words i.e '[a-zA-Z0-9_]'

#### Match
```python
import re
#   match a date string
regex = r'([a-zA-Z]+) (\d+)'
if re.search(regex, "June 24"):
    match = re.search(regex, "June 20")
    print('Match at index %s, %s' % (match.start(), match.end()))
```
#### Findall
```python
import re
txt = 'This is a nice example, isn't it?'
x = re.findall('is', txt)
print(x))
```
```python
import re
regex = r'[a-zA-Z]+ \d+'
matches = re.findall(regex, 'December 21, August 10, January 2')
for match in matches:
    print('Full match: %s' % (match))

```

#### Search

```python 
import re
regex = re.compile(r'(\w+) World')
result = regex.search('Hello World this is a test')
if result:

    print(result.start(), result.end())

for result in regex.findall('1 World, 2 World, red World, blue World'):
    print(result)

print(regex.sub(r"\1 friends", "Hello World"))
```




## Lists
These provide a way of storing objects in an ordered sequence.  They are mutable, so objects can be redefined as needed.  The implimentation of a list in Python is very similar to arrays in other languages, but we do not have to worry about the type of object we are placing in the list:  any object can be placed in a list.  Read the following code and try to guess what the result will be:

``` python
L=['string1', 123.0,'string2']
print(L[0])
print(L[1:])
print(L[:1])
print(L+[1.0,200,'string3'])
print(L) #just to prove the original list hasn't changed
L[0]='New String!'
print(L) #now the first entry has changed.  pretty cool
```
Notice this next example will not work since the operation of adding the value 2 to a list an ambiguous (even if the list is all numbers)
``` python
L=['string1', 123.0,'string2']
print(L+2)
#   TypeError: can only concatenate list (not "int") to list
```

### List Methods of Interest
In the previous examples, it was shown that lists could be joined together by the **+** operator.  If we wish to add an object to a list first creating a list to hold it, just the **append()** method.  Similarly , the **pop()** method will remove the object from the list at a given position and return it.

``` python
L=['string1', 123.0,'string2']
L.append('last string')
print(L)

L2=L.pop(1)
print(L)
print(L2)
```


There are also **sort()** and **reverse()** methods that can be pretty helpful if needed.  Object types must be considered for the sort function, since it might not make sense to try to compare a string to an integer.  Also, the sort method will always prioritize capital letters over lower case letters, which may be of concern when doing some serious string parsing. 

Now that we have some familiarity of 2 Python types, we can explore an example of converting one into another.  First a list of characters will be converted into a string, using the **join()** method and then separated back into a list using the **list** function.  **join** works on a string 'separator', and will iterate over the object placed in the method.  If the separator is empty, then the objects will be placed right next to each other.

``` python
L1 = ['a', 'b', 'c', 'd']
separator = ''
S1 = separator.join(L1)
print(S1, type(S1))
L2 = list(S1)
print(L2, L1==L2)
```
Now, using only this knowledge, we can use the lists **reverse()** method to reverse a string
```python
S1='abcd'
L1 = list(S1)
L1.reverse()
S2 = ''.join(L1)
print(S2)
```
Spolier alert:  there is a better way of writing this...
```python
s1='test to reverse'
print(s1[::-1])
#   esrever ot tset
```
### Nesting Lists
Since arbitrary objects can be placed in a list, you can make a list of lists.  These can be built in a way similar to trees or matricies, although there are better alternatives for both structures in python.
```python
M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
#   print first row
print(M[0])
```

### Comprehensions
Comprehensions are similar to the set-builder notation used in mathematics, and can be used to map and filter lists in python.  The following example will print out the column vector of matix M defined above.  Comprehensions can be used with lists, sets, dictionaries, and generators.
```
#   print middle element 
print(M[1][2])
```

From the example above, its easy to see that working with rows is really easy; they can be selected by using their indicies.  To get a column of the matrix though, we have to go into each row list and select the nth element and return it in a list.  This involves comprehensions.
```python
#   print second column
col2=[row[1] for row in M]
print(col2)
```
In the code above, notice that we are looking over each row and returning the value of row(1).  More complicated expressions can be made by changing the expressions for the value returned or how we filter the data.
```python
#   make a list of the value col2+1
col2=[row[1]+1 for row in M]
print(col2)
```
```python
#   make a list of the value col2^2 if odd
col2=[row[1]**2 for row in M if row[1]%2!=0]
print(col2)
```
These last few examples have shown comprehensions used to filter matrix M.  Compresensions are also useful in generating new lists, as shown in the following examples.  Notice that **list(range(4))** makes the list [0,1,2,3]
```python
#   some more complex comprehensions with lists
L1=[[x*10,x**2] for x in range(4)]
L2=[[x**2,x,x**-2] for x in range(10,1,-2)]
print(L1,L2)
```
Comprehensions can be inclosed in parentheses to make a generator
```python
#   sum the rows in M
G = (sum(row) for row in M)
print(next(G),next(G),next(G))
``` 

## Dictionaries
With lists, objects could be refered to with an index position that was ordered zero to n.  Dictionaries do not have a numerical index so they lack the sense of order lists have. Instead they feature a 'key' that will reference a corresponding value.  Below are three ways of creating/adding to a dictionary.

```python
D1 = {'name': 'Sky', 'age': '25', 'job': 'dev'}
print (D1['name'])
D2 = dict(name='Sky', age=25, job='dev')
print (D2['name'])
D3 = {}
D3['name'] = 'Sky'
D3['age'] = 25
D3['job']='dev'
print (D3['name'])
``` 

## Tuples
Tuples represent a group of objects and are immutable like strings. They can be indexed and manipulated similarly to lists.

```python
#   Creating and manipulating tuples
T = (1,2,3,4)
T = T + (5,6)
print (T)
print(T.index(3))
print(T.count(3))
``` 
## Files
To create a basic text file and save, we must 'open', 'write', and 'close' a file:
```python
f = open('data1.txt', 'w')   #'w' is for writing
f.write('This is an example file\n')
f.close()
``` 
Now to open the text and read in our one line string:
```python
f = open('data1.txt')   #'r' for read is the default
textIn = f.read()
print(textIn)
``` 


This is cool, but note that this is a very basic example.  We are reading and writing to the same location that our program is executed from; for most data processing exmples we would most likely keep all data somewhere far from the program location and possible in various locations.  We are also just writing a single string to the file and extracting a single string.  This is not very helpful if we have a page of delineatd data or a binary file.`


These are the access modes used with files:
| Test | Description |
| ------ | ----------- |
| r   | read only |
| rb | read binary|
| r+    | read + write|
| rb+  | read + write binary |
| w   | write only |
| wb | write binary|
| w+    | write + read|
| wb+  | write + read binary |
| a   | append only |
| ab | append binary|
| a+    | append + read|
| ab+  | append + read binary |

### Binary Byte File Example
I will talk about binary files more when there is a reason to, but I think it is helpful to include this example.
```python
import struct
#   example 1
packed = struct.pack('>i4sh', 7, b'spam', 8)
#print(packed)
file = open('data.bin', 'wb')
file.write(packed)
file.close()

#   now we can open the file
dataIn = open('data.bin', 'rb').read()
print(dataIn[4:8])

#   example 2
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

f=open("binfile.bin","rb")
num=list(f.read())
print (num)
f.close()
``` 
### Unicode Text Files
Python defaults to ascii, but unicode is also supported.  UTF-8 is used in 95% of the internet because it supports so many characters.  The first 128 Unicode code points represent the ASCII characters.

```python
#   make a unicode character and write to file
print('\xc4')
S = 'test unicode:  ' + '\xc4'
file = open('uni.txt', 'w', encoding = 'utf-8')
file.write(S)
file.close()
``` 


