# Chaper 4 Solutions
### 1.)  What are the core data types in Python?
1. Numbers
    * integer
    * floating point
    * complex
    * fractional
    * decimal
2. Strings
    * text string
    * byte string
3. Lists
4. Dictionaries
5. Tuples
6. Files
7. Sets
8. Boolean

### 2.)  What are some examples of non-core data types?
1. User defined types
2. types from packages like NumPy
### 3.)  Why are some types "core" types and others not?
These types are part of the Python language and are always available
### 4.)  What does immutable mean?  What are the immutable core types?
Immutable objects cannot be changed once they are written.  To manipulate the contents of an immutable object like a string, the string must be copied into a new location with the changes being made.  The immutable core types are:
 1. Numbers
 2. Strings
 3. Tuples
 ### 5.)  What is a sequence and which types are sequential?
A sequence in this context is a numerically ordered set of objects.  These have indicies that start at 0 and go for the length of the structure. Objects in the structure can be found using the corresponding indicies.  These are iterable, meaning that when we specify one object in an iterable structure, there is a **next** object linked to it.  This way we can apply maps and loops over the object.  The sequential types in Python are:
1. Strings
2. Lists
3. Tuples
### 6.)  Define "mapping".  Which type in Python is a mapping?
Mapping denotes an object that associates keys to values.  The dicitionary is the only core type that can do this
### 7.)  Define "polymorphism".  What does this mean w.r.t. coding in Python?
Polymorphism gives a function or an operation a definition based on the context it is used. 
An operation like ** * ** can have different meanings based on the types of objects, e.g. with strings or numbers.
