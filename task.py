Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#task
a=["code","codegnan","python"]
#["CODE","CODEGNAN","PYTHON"]
print(a)
['code', 'codegnan', 'python']
print(a.upper())
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(a.upper())
AttributeError: 'list' object has no attribute 'upper'
a[::]
['code', 'codegnan', 'python']
a.capitalize()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.capitalize()
AttributeError: 'list' object has no attribute 'capitalize'
a.title()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.title()
AttributeError: 'list' object has no attribute 'title'
a[::upper]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[::upper]
NameError: name 'upper' is not defined. Did you mean: 'super'?
b=str(a)
b
"['code', 'codegnan', 'python']"
b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
a=[9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,5,2,1]
a[::5]
[9, 4]
a[::-1]
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
a[::-2]
[0, 3, 4, 2, 1]
a[::-1]
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
a[1:11:1]
[1, 5, 2, 8, 4, 6, 3, 7, 0]
a[::-1]
[0, 7, 3, 6, 4, 8, 2, 5, 1, 9]
a[1::2]
[1, 2, 4, 3, 0]
a[1::]
[1, 5, 2, 8, 4, 6, 3, 7, 0]
len(a)
10
print(a)
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
a1=a[0:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:10]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a2.sort()
a2
[0, 3, 4, 6, 7]
a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> b=a2+a1
>>> b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
>>> 
>>> a=["code","codegnan","python"]
>>> b=str(a)
>>> b.upper()
"['CODE', 'CODEGNAN', 'PYTHON']"
>>> 
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:10]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a2.sort()
>>> a2
[0, 3, 4, 6, 7]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> b=a2+a1
>>> b
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
