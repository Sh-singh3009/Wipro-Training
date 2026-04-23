Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id(s1)
2722611738448
s2='hi'
id(s2)
140708306171320
s3=s1
id(s3)
2722611738448
s3
'hello'
s1='hi'
id(s1)
140708306171320



list1=[10,20,30,40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
list[-1]
list[-1]
list1[-1]
40
list1[0:3]
[10, 20, 30]
KeyboardInterrupt
list1[0:3:2]
[10, 30]
s1='india'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3=list1
list3
[10, 20, 30, 40]
id(list1)
2722595457984
id(list3)
2722595457984
list4=[100,'hi',100,True,69.36]
list4
[100, 'hi', 100, True, 69.36]
list4[2]=23
list4
[100, 'hi', 23, True, 69.36]
list4[5]='hey'
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list4[5]='hey'
IndexError: list assignment index out of range
list4[0]=list4[1]=100
list4
[100, 100, 23, True, 69.36]
list4[1]='hi'
list4
[100, 'hi', 23, True, 69.36]
list1
[10, 20, 30, 40]
list1.append('hey')
list1
[10, 20, 30, 40, 'hey']
list1.remove(4)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list1.remove(4)
ValueError: list.remove(x): x not in list
list4.count(23)
1
list1.insert(2,200)
list1
[10, 20, 200, 30, 40, 'hey']
id(list1)
2722595457984
list1.pop()
'hey'
list1
[10, 20, 200, 30, 40]
list1.pop(2)
200
list1
[10, 20, 30, 40]
list2
['i', 'n', 'd', 'i', 'a']
list2.clear()
list2
[]
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?



tuple1=(11,22,33,44,55)
tuple
<class 'tuple'>
tuple1
(11, 22, 33, 44, 55)
tuple[3]
tuple[3]
tuple1[6]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tuple1[6]
IndexError: tuple index out of range
tuple[2]=77
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    tuple[2]=77
TypeError: 'type' object does not support item assignment
tuple1[0:4:2]
(11, 33)
tuple1.index(44)
3
tuple1.count(22)
1
tuple2=tuple1
tuple2
(11, 22, 33, 44, 55)
tuple3=tuple(list1)
tuple3
(10, 20, 30, 40)
list1.append(tupple1)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list1.append(tupple1)
NameError: name 'tupple1' is not defined. Did you mean: 'tuple1'?
list1.append(tuple1)
list1
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
list1[4].[1]
SyntaxError: invalid syntax
list1[3][3]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list1[3][3]
TypeError: 'int' object is not subscriptable
list1
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
list1[4][3]
44



set1={10,20,30,40,50}
set1
{50, 20, 40, 10, 30}
set1[2]
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
set1.add(25)
set1
{50, 20, 40, 25, 10, 30}
set1.add('25')
set1
{50, 20, 40, 25, 10, '25', 30}
set1={10,20,30,40,50}
set1.add('25')
set1.add(25)
set1
{50, 20, 25, 40, '25', 10, 30}
set2=set(set1)
set2
{50, 20, 25, 40, '25', 10, 30}
set2.remove('25')
set2
{50, 20, 25, 40, 10, 30}
set1
{50, 20, 25, 40, '25', 10, 30}
set1.union(set2)
{40, '25', 10, 50, 20, 25, 30}
set1.intersection(set2)
{40, 10, 50, 20, 25, 30}
l1=[1,2,3,4,5]
l1
[1, 2, 3, 4, 5]
t1=(10,20,30,40,50,60,70)
t1
(10, 20, 30, 40, 50, 60, 70)
t1.add(l1)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    t1.add(l1)
AttributeError: 'tuple' object has no attribute 'add'
t2=tuple(l1)
t2
(1, 2, 3, 4, 5)
l1.add(t1)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    l1.add(t1)
AttributeError: 'list' object has no attribute 'add'
l1.append(t1)
l1
[1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70)]
t2=(11,[1,2,3],22,33)
t2[1]
[1, 2, 3]
t1=t1+l1
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    t1=t1+l1
TypeError: can only concatenate tuple (not "list") to tuple
t1=t1+l1,
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    t1=t1+l1,
TypeError: can only concatenate tuple (not "list") to tuple
t3=t1+l1
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    t3=t1+l1
TypeError: can only concatenate tuple (not "list") to tuple
t3=t1+l1,
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    t3=t1+l1,
TypeError: can only concatenate tuple (not "list") to tuple
t1=tuple(l1)
t1
(1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70))
l1=list(t1)
l1
[1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70)]
set1
{50, 20, 25, 40, '25', 10, 30}
set1.isdisjoint()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    set1.isdisjoint()
TypeError: set.isdisjoint() takes exactly one argument (0 given)
set1.isdisjoint(1)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    set1.isdisjoint(1)
TypeError: 'int' object is not iterable
list1
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
list2
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list3
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
tuple1
(11, 22, 33, 44, 55)
tuple2
(11, 22, 33, 44, 55)
tuple3
(10, 20, 30, 40)
l1
[1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70)]
l2
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    l2
NameError: name 'l2' is not defined. Did you mean: 's2'?
t1
(1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70))
t2
(11, [1, 2, 3], 22, 33)
t3
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    t3
NameError: name 't3' is not defined. Did you mean: 's3'?
l1
[1, 2, 3, 4, 5, (10, 20, 30, 40, 50, 60, 70)]
l1[5][2]=33
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    l1[5][2]=33
TypeError: 'tuple' object does not support item assignment
dict
<class 'dict'>
dict1={1:10,2:20,3:30}
dict1
{1: 10, 2: 20, 3: 30}
dict1[1]
10
dict2={'a':10,'b':20,'c':30}
>>> dict2['b']
20
>>> stud={'rno':101,'name':'AAA', 'city':'BBB'}
>>> stud
{'rno': 101, 'name': 'AAA', 'city': 'BBB'}
>>> stud['name']
'AAA'
>>> stud['name']='XXX'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
>>> stud['fname']='yyy'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB', 'fname': 'yyy'}
>>> stud.get('name')
'XXX'
>>> stud.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> stud.values()
dict_values([101, 'XXX', 'BBB', 'yyy'])
>>> stud.pop('fname')
'yyy'
>>> stud
{'rno': 101, 'name': 'XXX', 'city': 'BBB'}
