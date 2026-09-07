Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="data science"
a[::]
'data science'
a{::1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a[::1]
'data science'
a[::2]
'dt cec'
b="machine learning"
a[::3]
'dacn'
b[::3]
'mheeng'
b[::5]
'mnag'
b[::2]
'mcielann'
b[::9]
'me'
>>> b[3:11]
'hine lea'
>>> b[5:]
'ne learning'
>>> b[:7]
'machine'
>>> c='cloud computing'
>>> c[1:7:2]
'lu '
>>> a[2:13:3]
'tsee'
>>> del a
>>> c[2:13:3]
'o mt'
>>> c[4:14:5]
'dp'
>>> c[3:12:6]
'up'
>>> 
>>> a="python course"
>>> a[-1:-9:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-4:-13:-5]
'uo'
>>> a[-6:-12:-2]
'cnh'
>>> #donts
>>> a[7:3:2]
''
>>> a[3:7:2]
'hn'
>>> a[-9:-5:-2]
''
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
