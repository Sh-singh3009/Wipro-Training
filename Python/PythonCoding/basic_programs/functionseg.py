"""
Date: 23-04-2026
Desc: functions
"""
#functions
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div():
    pass


#ARBITRARY ARGUMENTS
def addition(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


#OPTIONAL ARGUMENTS
def add1(n1, n2, n3=10):
    return n1 + n2 + n3

#driver
num1=int(input('Enter a number: '))
num2=int(input('Enter another number: '))

res = add(num1, num2)
print('Add: ', res)

res = sub(num1, num2)
print('Sub: ', res)
res = sub(num2, num1)       #positional arguments
print('(pos arg) Sub: ', res)
res = sub(n2=num2, n1=num1)     #keyword arguments
print('(keyword arg) Sub: ', res)

res = mul(num1, num2)
print('Mul: ', res)




'''numbers = list()
count = int(input('Enter how many numbers you want in list: '))'''

'''for _ in range(1, count+1):
    numbers.append(int(input('No: ')))'''
#ARBITRARY
print('arbitrary arg(addn of n nos)', addition(5,6,9))
print('arbitrary arg(addn of n nos)', addition(5,6))
print('arbitrary arg(addn of n nos)', addition(5,6,9,3,10,8,7,23))

#OPTIONAL ARGUMENTS
print('optional arg', add1(num1, num2))
print('optional arg', add1(num1, num2, 100))



#LAMBDA FUNCTIONS

add_lamb = lambda n1, n2 :n1 + n2

print('lambda function', add_lamb(num1,num2))

numbers1 = [1,2,3,4,5,6,7,8,9,10]
#To square the values even nos in numbers1 list
#sq = lambda nums : [num * num for num in nums]
#print('lambda function', tuple( sq(numbers1) ))
sq = lambda nums : [num * num for num in nums if num%2 == 0 ]
print('lambda function', sq(numbers1))