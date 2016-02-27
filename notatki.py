# Microsoft Windows [Version 10.0.10586]
# (c) 2015 Microsoft Corporation. All rights reserved.
#
# C:\Users\Kunia>mkdir djangogirls
# A subdirectory or file djangogirls already exists.
#
# C:\Users\Kunia>cd djangogirls
#
# C:\Users\Kunia\djangogirls>python3 -m venv myvenv
# 'python3' is not recognized as an internal or external command,
# operable program or batch file.
#
# C:\Users\Kunia\djangogirls>C:\Python34\python -m venv venv
#
# C:\Users\Kunia\djangogirls>C:\Python34\python -m venv myvenv
#
# C:\Users\Kunia\djangogirls>myvenv\Scripts\activate
# (myvenv) C:\Users\Kunia\djangogirls>pip install django==1.8
# You are using pip version 6.0.8, however version 8.0.3 is available.
# You should consider upgrading via the 'pip install --upgrade pip' command.
# Collecting django==1.8
#   Downloading Django-1.8-py2.py3-none-any.whl (6.2MB)
#     100% |################################| 6.2MB 44kB/s
# Installing collected packages: django
#
# Successfully installed django-1.8
#
# (myvenv) C:\Users\Kunia\djangogirls>python
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2+3
5
>>> 4*5-5-1-40/2
-6.0
>>> 6+8*2
22
>>> 'Michalina'
'Michalina'
>>> 'Hej'+'Michalina'
'HejMichalina'
>>> 'Hej '+'Michalina'
'Hej Michalina'
>>> "Michalina" * 4
'MichalinaMichalinaMichalinaMichalina'
>>> "Runnin' down the hill"
"Runnin' down the hill"
>>> "Runnin\' down the hill"
"Runnin' down the hill"
>>> 'Michalina'.upper()
'MICHALINA'
>>> len('Michalina')
9
>>> len(304023)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> len(str(304023))
6
>>> int(123)
123
>>> int(monika)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'monika' is not defined
>>> int(245)
245
>>> int('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'hello'
>>> int(123)
123
>>> a=123
>>> int(a)
123
>>> a
123
>>> imie='Michalina'
>>> imie
'Michalina'
>>> len(imie)
9
>>> b=3
>>> a*b
369
>>> print(imie)
Michalina
>>> imie
'Michalina'
>>> []
[]
>>> wynik=[3,42,12,19,30,59]
>>> len(wynik)
6
>>> wyniki.sort
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wyniki' is not defined
>>> wynik.sort
<built-in method sort of list object at 0x0000000002ACCD48>
>>> wyniki.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wyniki' is not defined
>>> wynik.sort()
>>> print(wyniki)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wyniki' is not defined
>>> print(wynik)
[3, 12, 19, 30, 42, 59]
>>> wynik.reverse()
>>> print(wynik)
[59, 42, 30, 19, 12, 3]
>>> wynik.append(199)
>>> print(wynik)
[59, 42, 30, 19, 12, 3, 199]
>>> print(wynik[0])
59
>>> print(wynik[1])
42
>>> print(wyniki)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wyniki' is not defined
>>> print(wynik)
[59, 42, 30, 19, 12, 3, 199]
>>> print(wynik[0])
59
>>> del wyniki[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'wyniki' is not defined
>>> del wynik[0]
>>> print(wynik)
[42, 30, 19, 12, 3, 199]
>>> print(wynik[12])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> {}
{}
>>> uczestniczka={'imie':'Miska', 'kraj':'Polska','ulubione_liczby':[7,42,92]}
>>> uczestniczka
{'imie': 'Miska', 'ulubione_liczby': [7, 42, 92], 'kraj': 'Polska'}
>>> print(uczestniczka['imie'])
Miska
>>> uczestniczka['wiek']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'wiek'
>>> uczestniczka['ulubiony_jezyk']='Python'
>>> len(uczestniczka)
4
>>> del uczestniczka['ulubione_liczby']
>>> uczestniczka
{'imie': 'Miska', 'kraj': 'Polska', 'ulubiony_jezyk': 'Python'}
>>> uczestniczka['kraj']='Szwecja'
>>> uczestniczka
{'imie': 'Miska', 'kraj': 'Szwecja', 'ulubiony_jezyk': 'Python'}
>>> 5>2
True
>>> 3<1
False
>>> 5>2*2
True
>>> 1==1
True
>>> 5!=2
True
>>> 6>=12/2
True
>>> 3<=2
False
>>> 6>2 and 2<3
True
>>> 3>2 and 2<1
False
>>> 1>'django'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
>>> a=True
>>> a
True
>>> a=2>5
>>> a
False
>>> True and True
True
>>> True ad False
  File "<stdin>", line 1
    True ad False
          ^
SyntaxError: invalid syntax
>>> True and False
False
>>> True or False
True
>>> True or 1==1
True
>>> 1!=2
True
>>> len(str(304023))
6
>>> 2>len(str(304023))
False
>>> 7>len(str(304023))
True
>>>exit()
$
