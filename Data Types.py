Python 3.15.0 (v3.15.0:d220409a13b, Oct  9 2026, 08:17:44) [Clang 21.0.0 (clang-2100.1.1.101)] on darwin
Enter "help" below or click "Help" above for more information.
#int()
int(9)
9
int(7.8)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(6+9)
15
int(6+8j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> int(True)
1
>>> int(False)
0
>>> #float()
>>> float(9)
9.0
>>> float(8.9)
8.9
>>> float("hi")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
>>> float(6+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #complex()
>>> complex(8)
(8+0j)
>>> complex(8.9)
(8.9+0j)
>>> complex(6=9j)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> complex(6+9j)
(6+9j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #str()
>>> str(8)
'8'
>>> str(7.9)
'7.9'
>>> str(7+9j)
'(7+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #bool()
>>> bool(9)
True
>>> bool(8.9)
True
>>> bool(8,9)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    bool(8,9)
TypeError: bool expected at most 1 argument, got 2
>>> bool(True)
True
>>> bool(False)
False
