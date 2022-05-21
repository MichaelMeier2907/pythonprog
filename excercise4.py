Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4+5
9
>>> a = 6-4
>>> print(a)
2
>>> type(a)
<class 'int'>
>>> a="michael"
>>> print(a)
michael
>>> type(a)
<class 'str'>
>>> a=5**3
>>> print(a)
125
>>> a=TRUE
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
>>> a=True
>>> print(a)
True
>>> type(a)
<class 'bool'>
>>> for i in range(5):
... print(i)
  File "<stdin>", line 2
    print(i)
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in range(5):
... b +=1
  File "<stdin>", line 2
    b +=1
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for i in range(5):
... 	print(i)
... 
0
1
2
3
4
>>> for i in range(5):
... {print(i)}
  File "<stdin>", line 2
    {print(i)}
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> print(a)
True
>>> b=false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> b=False
>>> c=a AND b
  File "<stdin>", line 1
    c=a AND b
        ^^^
SyntaxError: invalid syntax
>>> c=(a AND b)
  File "<stdin>", line 1
    c=(a AND b)
       ^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a<b
False
>>> b<a
True
>>> a IS boolean
  File "<stdin>", line 1
    a IS boolean
      ^^
SyntaxError: invalid syntax
>>> a IS "boolean"
  File "<stdin>", line 1
    a IS "boolean"
      ^^
SyntaxError: invalid syntax
>>> 