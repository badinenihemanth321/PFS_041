Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#Arthematic
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a%b)
4
print(a**b)
4096

#Assignment
a=3
b=6
a+=b
a
9
a-=2
a
7
a*=3
a
21
a//=4
a
5
a/=4
a
1.25
a%=2
a
1.25
a**=2
a
1.5625
b
6
b+=3
b
9
b-=2
b
7
b*=5
b
35
b//=5
b
7
b/=5
b
1.4
b%=5
b
1.4
b**2
1.9599999999999997

#Comparision
a=8
b=10
a>b
False
b<a
False
a<b
True
b>a
True
a!=b
True
a==b
False
a<=b
True
b>=a
True
a>=b
False
b<=a
False

#Logical
a=5
b=10
a<b and b>a
True
a>b and b<a
False
a<=b and b>=a
True
a>=b and b<=a
False
a!=b and a==b
False
a<b or b<a
True
a<=b or b>=a
True
not True
False
not False
True
a!=b or a==b
True

#Identify
a=4
type(a) is int
True
type(a) is not int
False
b=0.6
type(b) is not float
False
type(b) is float
True

#Membership
a=3,4,5,6,7,8,9
7 in a
True
2 not in a
True
2 in a
False

#Bitwise
a=5
b=10
bin(a)
'0b101'
bin(b)
'0b1010'
a&b
0
a=6
del a
>>> a=2
>>> b=6
>>> bin(a)
'0b10'
>>> bin(b)
'0b110'
>>> a&b
2
>>> a=9
>>> b=7
>>> a|b
15
>>> a=4
>>> ~a
-5
>>> a=6
>>> del a
>>> a=-6
>>> ~a
5
>>> a=3
>>> b=5
>>> a^b
6
>>> a=6
>>> b=8
>>> a^b
14
>>> a=6
>>> a<<
SyntaxError: invalid syntax
>>> a<<3
48
>>> a=3
>>> a>>3
0
>>> a=7
>>> a>>2
1
