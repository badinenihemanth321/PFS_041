#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''

'''a=40
b=60
if a>b:
    print("less")'''

'''a=50
b=80
if b>a:
    print("greater")'''

'''a=5
b=9
if a<=b:
    print("greater")'''

'''a=11
b=13
if a>=b:
    print("less")'''

'''a=7
b=8
if a!=b:
    print("not equal")'''

'''a=5
b=5
if a==b:
    print("equal")'''

'''a="python"
if a=="python":
    print("true")
'''

'''a="java"
if a!="python":
    print("false")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a>30:
    print("greater")'''


#if-condition by using logical operators
#and,or,not
'''a=4
b=8
if a<b and b>a:
    print("less")'''

'''a=6
b=9
if a<=b and b>=a:
    print("true")'''

'''a=7
b=10
if a!=b and b==a:
    print("less")'''

'''a=12
b=14
if a<b or b>a:
    print("less")'''

'''a=15
b=20
if a<=b or b>=a:
    print("true")'''

'''a=10
b=20
if a!=b or b==a:
    print("true")'''

'''a=3
b=5
if not a<b:
    print("true")'''

'''a=3
b=5
if not a>b:
    print("true")'''

'''a=3
b=5
if not a<b and b>a:
    print("true")'''

'''a=int(input("a value"))
b=int(input("b value"))
if not a<b:
    print("true")'''


#by using identify operators
#id,is not
'''a=10
if type(a) is int:
    print("int")'''


'''a=7
if type(a) is not int:
    print("it is not int")'''


'''a=10.5
if type(a) is not int:
    print("it is not int")'''


'''a=int(input("a value"))
if type(a) is int:
    print("int")'''


#by using membersing operators
#in,not in
'''a=[2,3,4,5,6,7,8,9,10]
if 5 in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 10 not in a:
    print("true")'''

'''a=[2,3,4,5,6,7,8,9,10]
if 15 not in a:
    print("true")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")#error'''

'''a=[2,3,4,5,6,7,8,9,10]
b=int(input())
if b in a:
    print("true")'''

#if-else by using comparision operators

'''a=5
b=9
if a<b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a>b:
    print("less")
else:
    print("false")'''

'''a=5
b=9
if a!=b:
    print("not equal")
else:
    print("equal")'''

'''a=5
b=9
if a==b:
    print("equal")
else:
    print("not equal")'''


#logical operators
#and,or,not

'''a=5
b=9
if a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=5
b=9
if a>b or b<a:
    print("true")
else:
    print("false")'''

'''a=5
b=9
if not a>b and b>a:
    print("true")
else:
    print("false")'''


#by using membership operators
#is,is not

'''a=3
if type(a) is int:
    print("int")
else:
    print("not int")'''

'''a=10
if type(a) is not int:
    print("int")
else:
    print("not int")'''

#by using identify operators
#in,not in
'''a=[1,2,3,4,5,6,7,8,9]
if 5 in a:
    print("in")
else:
    print("not in")'''

'''a=[1,2,3,4,5,6,7,8,9]
if 5 not in a:
    print("in")
else:
    print("not in")'''




#if-elif-else conditions by using comparision operators
'''a=2
b=4
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''

'''a=5
b=6
if a>b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''

'''a=9
b=12
if a==b:
    print("equal")
elif b<a:
    print("less")
else:
    print("true")'''


'''a=3
b=5
if a>b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("false")'''


#by using logical operators
#and,or,not
'''a=6
b=5
if a<b and b<a:
    print("less")
elif a<b or b<a:
    print("greater")
elif not a<b and b<a:
    print("true")
else:
    print("false")'''


#by using identify operators
#is,is not
'''a=10
b=20
if type(a) is float:
    print("float")
elif type(b) is not float:
    print("int")
else:
    print("failed")'''


#by using identify operators
#in,not in
'''a=[1,2,3,4,5,6,7,8,9]
if 10 in a:
    print("available")
elif 10 not in a:
    print("not available")
else:
    print("failed")'''



#mutiple-if
'''a=5
b=10
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=5
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("not equal")'''

#by using logical operators
'''a=10
b=15
if a<b and b>a:
    print("greater")
if a!=b or a==b:
    print("true")
if not a<=b and b>=a:
    print("false")'''


#by using identify operators
#is,is not
'''a=5
b=10
if type(a) is float:
    print("true")
if type(b) is int:
    print("yes")
if type(a) is not float:
    print("graet")'''

#membership operators
'''a=[1,2,3,4,5,6,7,8,9]
if 3 in a:
    print("yes")
if 7 in a:
    print("greater")
if 10 not in a:
    print("true")
    print("not equal")'''


#nested-if
'''a=6
b=12
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=6
b=12
if a>b:
    print("less")
if b>a:
    print("greater")'''


'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")'''

    
'''a=10
b=20
if a<b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("true")'''

'''a=30
b=50
if a>b:
    print("less")
    if b>a:
        print("equal")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a>b:
    print("less")
    if b==a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''

'''a=60
b=80
if a<b:
    print("less")
    if b>a:
        print("equal")
    else:
        print("false")
else:
    print("true")'''


a=60
b=80
if a<b:
    print("less")
    if b==a:
        print("equal")
    elif a!=b:
        print("not equal")
    else:
        print("false")
else:
    print("true")
