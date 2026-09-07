Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("java","program")
'python program'
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
b="CODE"
b.lower()
'code'
#capitalize()->first letter capital
c="java"
c.capitalize()
'Java'
#title()->All letters starting capital
a="i am in the class"
a.title()
'I Am In The Class'
a.capitalize()
'I am in the class'
#startswith
a="hello world"
a.startswith("h")
True
a.endswith("d")
True
#isalpha()-> is alphabet or not
a.isaplha()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
a.isalpha()
False
#because it contains space
a="helloworld"
a.isalpha()
True
#isdigit()
a.isdigit()
False
a=12345
a.isdigit()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="54321"
b.isdigit()
True
#isalphanum()->either alphabet or num
a.isalphanum()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.isalphanum()
AttributeError: 'int' object has no attribute 'isalphanum'
#isalnum()
a.isalnum()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.isalnum()
AttributeError: 'int' object has no attribute 'isalnum'
b.isalnum()
True
#strip
#lstrip(),rstrip()
a="          hemanth        "
a.strip()
'hemanth'
a.lstrip()
'hemanth        '
a.rstrip()
'          hemanth'

#concatenation
a="hemanth"
b="badineni"
print(a+b)
hemanthbadineni
print(a+" "+b)
hemanth badineni
print(a.title()+" "+b.title())
Hemanth Badineni
print((a+" "+b).title())
Hemanth Badineni

#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
#join()
a="vij","hyd","vzg"
"".join(a)
'vijhydvzg'
" ".join(a)
'vij hyd vzg'
"k".join(a)
'vijkhydkvzg'
b="Hello"
"k".join(b)
'Hkeklklko'

#formatting -> to add additional str
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
city="vij"
print("city is",city)
city is vij

#format
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello{}".format(a,b))
hello motu hellopatlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu

#fstring()
a="Ms"
b="Dhoni"
print(f"hello {a}{b}")
hello MsDhoni
print(f"hello {a} {b}")
hello Ms Dhoni
print(f"hello {a} hello {b}")
hello Ms hello Dhoni

>>> #Tasks
>>> fname="hemanth"
>>> lname="badineni"
>>> print((fname+lname).format())
hemanthbadineni
>>> print((fname+" "+lname).format())
hemanth badineni
>>> #fstring
>>> print(f"{fname} {lname}")
hemanth badineni
>>> #format
>>> print("firstname{} lastname{}".format(fname,lname))
firstnamehemanth lastnamebadineni
>>> print("firstname {} lastname {}".format(fname,lname))
firstname hemanth lastname badineni
>>> #answer
>>> print("Full Name is {} {}".format(fname,lname))
Full Name is hemanth badineni
>>> print(f"Full name is {fname} {lname}")
Full name is hemanth badineni
>>> 
>>> a=5
>>> b=2
>>> c=a+b
>>> print("the sum is {}".format(c))
the sum is 7
>>> print(f"the sum is {c}")
the sum is 7
>>> print("the sum is {} {}".format(a+b))
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    print("the sum is {} {}".format(a+b))
IndexError: Replacement index 1 out of range for positional args tuple
>>> print("the sum is {} {} {}".format(a,b,a+b))
the sum is 5 2 7
>>> print("the sum is {}".format(a+b))
the sum is 7
