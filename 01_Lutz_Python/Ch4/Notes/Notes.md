# Chapter Four:  Introducing Python Object Types


## Python as a Language

Python was designed by Guido van Rossum in 1991.  it is considered:
+ Interpreted:  The interpreter runs over a virtual machine and executes the code line by line and converts it into low level machine language. Since, the interpreted language runs over virtual environment, these languages are considered platform independent.
+ High-Level:  Uses abstraction to make programming closer to our natural written conventions (conpared to machine/assembly language)
+ Multi-Paradigm:  These languages are can be written in several of the following ways
+ Object Oriented:  uses the "object" to represent data or a structure.  Objects have a notion of self, thier own properties (fields), and possible routines (methods).  Think C++ and Java.
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
#### What are regular expressions
#### Match
#### Search
#### Split


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







abcd
efgh
ijkl
mnop 

into 

ponm
lkji
hgfe
dcba

## Dictionaries


## Tuples

## Files


