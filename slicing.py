Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Slicing
a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:7]
'gna'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="work until you succeed"
>>> a[5:10]
'until'
>>> a[15:]
'succeed'
>>> a[11:14]
'you'
>>> a[0:4]
'work'
>>> a="Vijayawada is a royal city"
>>> a[22:]
'city'
>>> a[16:21]
'royal'
>>> a[0:10]
'Vijayawada'
>>> a[11:13]
'is'
>>> a="Happy Teachers Day"
>>> a[:-13]
'Happy'
>>> a[-3:]
'Day'
>>> a[-12:-5]
'Teacher'
>>> a="vizag is a city of destiny"
>>> a[:-21]
'vizag'
>>> a[-15:-11]
'city'
>>> a[-7:]
'destiny'
