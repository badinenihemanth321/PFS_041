Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
a="python"
len(a)
6
a="python course"
len(a)
13
a=""
len(a)
0
a=" "
len(a)
1

#count
a="twinkle twinkle little star"
count
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("t")
5
>>> a.count("twinkle")
2
>>> a.count(" ")
3
>>> 
>>> #find a string
>>> a.find("t")
0
>>> a="python"
>>> a.find("y")
1
>>> a.find("o")
4
>>> 
>>> #escape sequences
>>> #\n-> new line
>>> #\t->tab space
>>> a="idno\nname\tmobileno\nmailid\nbranch\tcollege"
>>> print(a)
idno
name	mobileno
mailid
branch	college
>>> b="idno:25\nname:hemanth\tmobileno:9491361370\nbranch:cse\nmailid:bunnyhemanth321@gmail.com\tcollege:VIT"
>>> print(b)
idno:25
name:hemanth	mobileno:9491361370
branch:cse
mailid:bunnyhemanth321@gmail.com	college:VIT
