Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hEllO'
s1.casefold()
'hello'
s1='HeLLo'
s1.casfold()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1.casfold()
AttributeError: 'str' object has no attribute 'casfold'. Did you mean: 'casefold'?
s1.casefold()
'hello'
s1.count('l')
0
s1.count('L')
2
s1.count('y')
0
s1.endswith('o')
True
s1.endswith('O')
False
s1.find('L')
2
s1.index('w')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s1.index('w')
ValueError: substring not found
s1.isalpha()
True
s1.isdigit()
False
s1.join(' there')
' HeLLotHeLLohHeLLoeHeLLorHeLLoe'
s1
'HeLLo'
s1 = 'Hello there how are you'
s1.split('')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1
'Hello there how are you'
s1.split('')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.split(' ')
['Hello', 'there', 'how', 'are', 'you']
len(s1)
23
s1
'Hello there how are you'
s1[5]
' '
s1[23]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s1[23]
IndexError: string index out of range
s1.[-3]
SyntaxError: invalid syntax
s1[-3]
'y'
s1[0:5:1]
'Hello'
s1[0:5:2]
'Hlo'
s1[::1]
'Hello there how are you'
s1[::2]
'Hloteehwaeyu'
s1='abcdefghijkl'
s1
'abcdefghijkl'
s.[::2]
SyntaxError: invalid syntax
s1[0::2]
'acegik'
s1[::2]
'acegik'
s1[0::-2]
'a'
s1[4::-2]
'eca'

========== RESTART: C:/Wipro Training/Python/str1ex.py =========
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
>>> 
= RESTART: C:/Wipro Training/Python/str1ex.py
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
= RESTART: C:/Wipro Training/Python/str1ex.py
h
e
l
l
o
