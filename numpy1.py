Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> array1=np.numpy(3,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\micha\AppData\Local\Programs\Python\Python310\lib\site-packages\numpy\__init__.py", line 315, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'numpy'
>>> array1=np.array(3.5)
>>> array1=np.array(4,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Cannot interpret '6' as a data type
>>> array1=np.array([5,8])
>>> array2=np.array([3.7])
>>> print(array1)
[5 8]
>>> array3=array1+array2
>>> print(array3)
[ 8.7 11.7]
>>> array2=np.array([4,9])
>>> array3=array1+array2
>>> print(array3)
[ 9 17]
>>> product=array1*array2
>>> print(product)
[20 72]
>>> 