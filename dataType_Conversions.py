Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Datatypes convertions
>>> #int
>>> int(8)
8
>>> float(6)
6.0
>>> int(6.5)
6
>>> int("hemanth")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("hemanth")
ValueError: invalid literal for int() with base 10: 'hemanth'
>>> int(4+6j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(4+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> 
>>> #float
>>> float(7)
7.0
>>> float(3.9)
3.9
>>> float("badineni")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("badineni")
ValueError: could not convert string to float: 'badineni'
>>> float(7+5j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(7+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
0.0float(False)
SyntaxError: invalid decimal literal
#srtr
str(8)
'8'
str(8.4)
'8.4'
str("Hemanth")
'Hemanth'
str(7+6j)
'(7+6j)'
str(True)
'True'
str(False)
'False'

#complex
complex(7)
(7+0j)
complex(8.8)
(8.8+0j)
complex("Badineni")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex("Badineni")
ValueError: complex() arg is a malformed string
complex(7+9j)
(7+9j)
complex(True)
(1+0j)
complex(False)
0j

#bool
bool(4)
True
bool(5.9)
True
bool("hemanth")
True
bool(5+9j)
True
bool(True)
True
bool(False)
False
