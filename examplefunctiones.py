Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def spezFuncPrint():
... 	print("Michael")
... 	print("Meier")
... 	print("Hallo")
... 
>>> spezFuncPrint()
Michael
Meier
Hallo
>>> def spezFuncPrint1()
  File "<stdin>", line 1
    def spezFuncPrint1()
                        ^
SyntaxError: expected ':'
>>> def spezFuncPrint1():
... 	print("Guten Tag")
... 	print("mein Name ist Michael")
... 	return(5)
... 
>>> a=spezFuncPrint1()
Guten Tag
mein Name ist Michael
>>> print(a)
5
>>> def FuncSumme(int summand1, int Summand2):
  File "<stdin>", line 1
    def FuncSumme(int summand1, int Summand2):
                      ^^^^^^^^
SyntaxError: invalid syntax
>>> def FuncSumme(summand1, summand2)
  File "<stdin>", line 1
    def FuncSumme(summand1, summand2)
                                     ^
SyntaxError: expected ':'
>>> def FuncSumme(summan1, summand2):
... 	return(summan1+summand2)
... 
>>> b=FuncSumme(3.5, 5.7)
>>> print(b)
9.2
>>> 