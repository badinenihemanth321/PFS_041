Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#List[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=4.5
type(b)
<class 'float'>
c=[4.5]
type(c)
<class 'list'>

#methods
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]
b=["ds","cn","dbms"]
b.extend(["ai","ml"])
b
['ds', 'cn', 'dbms', 'ai', 'ml']
c=["white","black"]
c.insert(1,"red")
c
['white', 'red', 'black']
a=["apple","mango","banana"]
a.index("banana")
2
a.copy()
['apple', 'mango', 'banana']
b=a.copy()
b
['apple', 'mango', 'banana']
a=["hi","hello","namasthe","adabh"]
a.pop()
'adabh'
a
['hi', 'hello', 'namasthe']
a.pop("hello")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop("hello")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'hello'
#remove()
a.remove("hello")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.remove("hello")
ValueError: list.remove(x): x not in list
a
['hi', 'namasthe']
a.remove("hi")
a
['namasthe']

a=["vij","hyd","vzg","chennai"]
a.sort()
a
['chennai', 'hyd', 'vij', 'vzg']
b=[8,10,4,65,37,1,22]
b.sort()
b
[1, 4, 8, 10, 22, 37, 65]
c=[4,4.5,"hyd",3+6j,True,False]
c.sort()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
>>> a=["mango","banana","dragon","orange"]
>>> a.reverse()
>>> a
['orange', 'dragon', 'banana', 'mango']
>>> a=["c","c++","java"]
>>> #len
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> c=["java"]
>>> len(c)
1
>>> a.count(c)
0
>>> a.count("c")
1
>>> a="coconut"
>>> a.count("c")
2
>>> a=["python",".net","hadoop"]
>>> a.clear()
>>> a
[]
>>> a.append("hemanth")
>>> a
['hemanth']
