Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dictionary{}
a={"name":"Hemanth","city":"vijayawada"}
print(a)
{'name': 'Hemanth', 'city': 'vijayawada'}
type(a)
<class 'dict'>
b={"name","hemanth"}
type(b)
<class 'set'>

a={"year":2026,"month":"sep","date":9}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'sep', 9])
a.items()
dict_items([('year', 2026), ('month', 'sep'), ('date', 9)])
a["month"]
'sep'
a[sep]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[sep]
NameError: name 'sep' is not defined. Did you mean: 'set'?
a.get("month")
'sep'

#update()-> to add elements
a={"name":"hemanth","city":"vja"}
a.update({"mailid":"hemanth@gmail.com"})
a
{'name': 'hemanth', 'city': 'vja', 'mailid': 'hemanth@gmail.com'}
a.update({"course":"python"},{"branch":"cse"})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.update({"course":"python"},{"branch":"cse"})
TypeError: update expected at most 1 argument, got 2
a.update({"course":"python","branch":"cse"})
a
{'name': 'hemanth', 'city': 'vja', 'mailid': 'hemanth@gmail.com', 'course': 'python', 'branch': 'cse'}
#setdefault()
a={"hour":3,"min":10}
a.setdefault("sec",4)
4
a
{'hour': 3, 'min': 10, 'sec': 4}
#in setdefault() method -> we can add only one [key:value]

#pop()
a={"week":"wed","date":9}
a.pop()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("week")
'wed'
#popitem()
a={"country":"india","state":"ap"}
a.popitem()
('state', 'ap')
a.popitem("country")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.popitem("country")
TypeError: dict.popitem() takes no arguments (1 given)
a={"name":"hemanth","course":"python","duration":100}
a.copy()
{'name': 'hemanth', 'course': 'python', 'duration': 100}
len(a)
3
a.count("name")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a.index("course")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.index("course")
AttributeError: 'dict' object has no attribute 'index'
a.clear()
a
{}
a={"name":"hemanth",year"
   
SyntaxError: unterminated string literal (detected at line 1)
a={"name":"hemanth","year":2026,"name"="hemanth"}
   
SyntaxError: ':' expected after dictionary key
a={"name":"hemanth","year":2026,"name":"hemanth"}
   
a
   
{'name': 'hemanth', 'year': 2026}
#it removes duplicate values
...    
>>> a={"name":"hemanth","year":2026,"name"="venkatesh"}
...    
SyntaxError: ':' expected after dictionary key
>>> a={"name":"hemanth","year":2026,"name":"venkatesh"}
...    
>>> a
...    
{'name': 'venkatesh', 'year': 2026}
>>> #it picks from last
...    
>>> a={"name":"hemanth","year":2026,"name1":"hemanth"}
...    
>>> a
...    
{'name': 'hemanth', 'year': 2026, 'name1': 'hemanth'}
>>> #key names should be different values can be same
...    
>>> #multiple values
...    
>>> a={"idnos":[10,20,30],"names":["john","joe","ram"],"places":["vja","vzg","hyd"]}
...    
>>> a.keys()
...    
dict_keys(['idnos', 'names', 'places'])
>>> a.values()
...    
dict_values([[10, 20, 30], ['john', 'joe', 'ram'], ['vja', 'vzg', 'hyd']])
>>> a.items()
...    
dict_items([('idnos', [10, 20, 30]), ('names', ['john', 'joe', 'ram']), ('places', ['vja', 'vzg', 'hyd'])])
>>> print(a)
...    
{'idnos': [10, 20, 30], 'names': ['john', 'joe', 'ram'], 'places': ['vja', 'vzg', 'hyd']}
>>> type(a)
...    
<class 'dict'>
