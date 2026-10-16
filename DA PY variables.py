Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#variables
a=2
print(a)
2
b=5
print(b)
5
x=90
print(x)
90
Z=50
print(Z)
50
a9=20
print(a9)
20
name=sumanth
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=sumanth
NameError: name 'sumanth' is not defined
name="sumanth"
print(name)
sumanth
>>> city="vijayawada"
>>> print(city)
vijayawada
>>> country=india
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    country=india
NameError: name 'india' is not defined
>>> country="india"
>>> print(country)
india
>>> _=40
>>> print(_)
40
>>> a=2,3,4,5,6,7,8
>>> print(a)
(2, 3, 4, 5, 6, 7, 8)
>>> a,b,c=3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,b,c=3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 7)
>>> a,b,c=(3,4,5)
>>> print(a,b,c)
3 4 5
>>> a=2 3 4 5 6 7 8 9
SyntaxError: invalid syntax
>>> a=2,3,4,5,6,7,8,9
>>> print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
>>> first name="sumamnth"
SyntaxError: invalid syntax
>>> first_name=sumanth
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    first_name=sumanth
NameError: name 'sumanth' is not defined
>>> first_name="sumanth"
>>> print(first_name)
sumanth
>>> fname="sumanth"
>>> lname="naidu"
>>> print(fname+lname)
sumanthnaidu
>>> print(fname+""+lname)
sumanthnaidu
>>> print(fname+" "+lname)
sumanth naidu
>>> a,b,c=100
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a,b,c=100
TypeError: cannot unpack non-iterable int object
>>> a=b=c=100
>>> print(a,b,c)
100 100 100
>>> a=10
>>> print(a)
10
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a9'?
