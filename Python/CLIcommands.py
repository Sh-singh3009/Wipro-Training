Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=8
print(x);
8
x
8
type(x)
<class 'int'>
t=3.0
type(t)
<class 'float'>
a=1234567890987654321
type(a)
<class 'int'>
q='a'
q
'a'
type(q)
<class 'str'>
w="hi there"
w
'hi there'
q='b'
q
'b'

s2="""hi there....
how are you??
i am good"""
s2
'hi there....\nhow are you??\ni am good'
b1=true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b1=true
NameError: name 'true' is not defined. Did you mean: 'True'?
b1=True
b1
True
y=y+1
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    y=y+1
NameError: name 'y' is not defined
10//3
3
3//10
0
8//10
0
12/2
6.0
3.8/2
1.9
3.8//2
1.0
5 | 3
7
a=2
b=2.0
a=b
a==b
True
c=a=b
c
2.0
1 and 1
1
1 and 2
2
1 and 3
3
1 AND 0
SyntaxError: invalid syntax
0 and 1
0
1 and 0
0
1 and 1
1
0 and 0
0
p=None
type(p)
<class 'NoneType'>
not p
True
5&3
1
5|3
7
5^3
6
p is int
False
a=1
a is int
False
type(a) is int
True
int is int
True
float is int
False
b=1.0
a is b
False
~0
-1
~-1
0
~-2
1
a=2
float(a)
2.0
a
2
a=float(a)
a
2.0
a=int(a)
a
2
a=2.3
a=int(a)
a
2
a=2.9
a=int(a)
a
2
int(a)
2
c=type(a)
c
<class 'int'>
print(c)
<class 'int'>
s=str(a)
s
'2'
s="abxc"
m=int(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    m=int(s)
ValueError: invalid literal for int() with base 10: 'abxc'
bool(s)
True
print('addition:', 2+2)
addition: 4
print('ans'+'6')
ans6
print('age', 23)
age 23
print('a'+"'"+'s')
a's
input()
abcd
'abcd'
input()

''
p=input('Num:')
Num:23
p
'23'
>>> type(p)
<class 'str'>
>>> 
========= RESTART: C:/Wipro Training/Python/helloWorld.py ========
Hello World!
>>> 
= RESTART: C:/Wipro Training/Python/helloWorld.py
Hello World!
>>> 
= RESTART: C:/Wipro Training/Python/calculationPgm.py
Sum: 11
>>> 
= RESTART: C:/Wipro Training/Python/calculationPgm.py
Enter a=2
Enter a=9
Sum: 11
>>> 
= RESTART: C:/Wipro Training/Python/calculationPgm.py
Enter a=10
Enter b=20
Sum: 30
