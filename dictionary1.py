Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> akt_person={"Name":"Meier", "Vorname":"Michael", "Jahrgang":"1971"}
>>> akt_vorname=akt_person["Vorname"]
>>> print(akt_vorname)
Michael
>>> Q={(0,0):2, (0,1):5, (0,2):3, (1,1):7, (1,2):4, (2,2):8}
>>> for i=0 in range(3):
  File "<stdin>", line 1
    for i=0 in range(3):
         ^
SyntaxError: invalid syntax
>>> for i in range(3):
... 	for j in range(3):
... 		a=Q[(i,j)]
... 		print(a)
... 
2
5
3
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyError: (1, 0)
>>> Q[(1,0)]=9
>>> Q[(2,0)]=4
>>> Q[(2,1)]=7
>>> for i in range(3):
... 	for j in range(3):
... 		a=Q[(i,j)]
... 		print(a)
... 
2
5
3
9
7
4
4
7
8
>>> i=1
>>> for i in range(7):
... 	print(i)
... 
0
1
2
3
4
5
6
>>> 