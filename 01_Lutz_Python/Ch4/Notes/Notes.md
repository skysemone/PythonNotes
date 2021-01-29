# Chapter Two:  Introducing Python Object Types


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

x = 123
print(type(x))
<class 'int'>

x = 123.0
print(type(x))
<class 'float'>

x = 123.0
y = 4
print(type(x*y))
<class 'float'>

x = '12+3j'
print(type(x))
<class 'complex'>

x = 123==321
print(type(x))
<class 'bool'>

x = '123.0'
print(type(x))
<class 'str'>

x = (123.0,123,123)
print(type(x))
<class 'tuple'>

x=[1,2,3,4,5]
print(type(x))
<class 'list'>

x={1,2,3,4,5}
print(type(x))
<class 'set'>

x={1:'entry 1', 2:'entry 2', 'c': 'entry c'}
print(type(x))
<class 'dict'>



## Strings

Strings can be used to record names, words, and other textual information, but it can also be used to store other collections of data.  In either case, the most frequent operations on strings involving copying the string, separating it into smaller sub-strings, or conbining strings together.  Strings start at position '0' and continue to the position of the last letter in the defined string.

### Immutability and Object ID
Strings are immutable in python (and many other languages.)  This means that when a string in defined in memory, making any change to the string with code will not just make a similar change in the memory, but copy the string to a new position of memory with the changes made.  Lets say that we have string a='Immutable', and we wanted to add an 's' to the end.  c=a+'s' 'Immutables' will cause a whole new string to be made.  The consequences of this will be highlighted in the follwing examples

The fastest way to show this is by trying to change a letter in a string
a='test'
a[0]='b'  TypeError: 'str' object does not support item assignment

but you can do something like this in a list:

a=['t', 'e','s','t']
a[0]='b'
print(a)
 
 What you can do is select part of the string and add it to another part:
 a='test'
 b='b'+a[1:]
 print(b)
 >>>'best'
 
 This is a good place to bring up '==' and 'is' in Python.  Every object defined in the Python code gets a unique ID upon creation.  In CPython this is the memory address, but using the standard implimentation, it is a constant value.  'is' should be used to check identity, and '==' used to check equalivance.  Using 'is' to compare two strings, in this case, is the equilivant to this statement using '=='

 id(a)==id(b)    <=>   a is b
 
 Python caches strings and objects to minimize space, so two different strings will still show up as the same id, while strings constructed through other means will not.
a='string 1'
b='string 1'
print(id(a), id(b))
>>> 4385830064 4385830064

a='string 1'
b=a[0:2]+a[2:5]
print(id(a), id(b))
>>>4372340336 4372236592

so in this instance, 'a==b' returns true, but 'a is b' returns false!
 

### Using Regular Expressions for Strings
#### What are regular expressions
#### Match
#### Search
#### Split


## Lists

## Dictionaries


## Tuples

## Files


