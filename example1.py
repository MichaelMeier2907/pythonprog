Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world");print("bye bye");
hello world
bye bye
>>> #this is hello world
>>> print("hello world");
hello world
>>> #statement in more than one line of code
>>> print("he\
... llo world");
hello world
>>> #variables
>>> ni_name = 'michael';
>>> mi_name = "michael";
>>> print(mi_name);
michael
>>> for i in range(5):
...   a+=1;
...   print(a);
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'a' is not defined
>>> 
>>> a = 1;
>>> for i in range(5):
...   a+=1;
...   print(a);
... 
2
3
4
5
6
>>> 