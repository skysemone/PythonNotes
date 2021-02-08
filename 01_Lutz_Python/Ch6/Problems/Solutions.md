# Chaper 6 Problems and Solutions
### 1.)  Consider the following; do they change the value printed for `A`?
  + A = "problem"
  + B = A
  + B = "test"
  ---
  
  **No change.**  When B is assigned the string "problem", its reference is pointed at the object A.  When reassigned to "test", B has a pointer to a new string, while A still points to "problem".
  
### 2.)  Consider the following; do they change the value printed for `A`?
+ A = ["problem"]
+ B = A
+ B[0] = "test"
---

**Yes, it changes A.**  In this case, the object that both A and B point to has been changed since lists are not immutable.  This can be seen in the following code:

```python
A = ["problem"]
B = A
B[0] = "test"
print(A,B)

A[0] = "new"
print(A,B)
```

### 3.)  Consider the following; do they change the value printed for `A`?
+ A = ["problem"]
+ B = A[:]
+ B = "test"
---

**No change.**  Since we are taking a slice of the list, B now points at the slice.
