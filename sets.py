Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #sets{}
>>> #it is unordered
>>> a={7,4.5,"python",5+9j,True,False}
>>> a
{False, True, (5+9j), 'python', 4.5, 7}
>>> type(a)
<class 'set'>
>>> b={7,9,4,0,1,4,7,9}
>>> b
{0, 1, 4, 7, 9}
>>> #it removes duplicate values
>>> a={4,5,6,7,8,9}
>>> a.add(10)
>>> a
{4, 5, 6, 7, 8, 9, 10}
>>> a={4,5,6,7,8,9}
>>> b={7,8,9}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> a={6,7,8,9,10,11,12}
>>> b={10,11,12}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> a={3,4,5,6,7}
>>> b={5,6,7,8,9,10}
>>> a.union(b)
{3, 4, 5, 6, 7, 8, 9, 10}
>>> a.intersection(b)
{5, 6, 7}
>>> #update() -> it updates value
>>> a={2,3,4,5,6}
>>> b={5,6,7,8,9,10}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
a
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b
{2, 3, 4, 5, 6, 7, 8, 9, 10}
#difference() -> prints diff values
a={6,7,8,9,10}
b={2,3,4,5,6,7,8}
a.difference(b)
{9, 10}
b.difference(a)
{2, 3, 4, 5}

#symmetric_difference()
a={7,8,9,10,11,12,13}
b={10,11,12,13,14,15}
a.symmetric_difference(b)
{7, 8, 9, 14, 15}
b.symmetric_difference(a)
{7, 8, 9, 14, 15}

a={3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference_update(b)
a
{3}
a
{3}
b.difference_update(a)
b
{4, 5, 6, 7, 8, 9, 10}

a={3,4,5,6,7,8}
b={1,3,6,7,8,9,10}
a.intersection_update(b)
a
{8, 3, 6, 7}
b.intersection_update(a)
b
{8, 3, 6, 7}
b
{8, 3, 6, 7}
a
{8, 3, 6, 7}
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(a)
a
set()
a.symmetric_difference_update(b)
a
{10, 11, 12, 13, 14, 15}
del a,b
a={6,7,8,9,10,11,12}
b={10,11,12,13,14,15}
a.symmetric_difference_update(b)
a
{6, 7, 8, 9, 13, 14, 15}
b.symmetric_difference_update(a)
b
{6, 7, 8, 9, 10, 11, 12}

#pop() and remove()
a={10,20,30,40,50}
a.pop()
50
a
{20, 40, 10, 30}
a.remove(10)
a
{20, 40, 30}
a.pop(30)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.pop(30)
TypeError: set.pop() takes no arguments (1 given)
a={4,5,6,7,8,9}
a.discard(8)
a
{4, 5, 6, 7, 9}
a.copy()
{4, 5, 6, 7, 9}
b=a.copy()
b
{4, 5, 6, 7, 9}
a
{4, 5, 6, 7, 9}
b
{4, 5, 6, 7, 9}
#clear() and add()
a={3,4,5,6,7}
a.clear()
a
set()
a.add(20)
a
{20}

#len()
a={5,6,7,8}
len(a)
4
a.index(4)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.index(4)
AttributeError: 'set' object has no attribute 'index'
a.count(5)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
#isdisjoint()
a={3,4,5,6,7}
b={2,3,5,6,7}
a.isdisjoint(b)
False
a={6,7,8,9}
b={1,2,3,4}
a.isdisjoint(b)
True
