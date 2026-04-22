"""
Date: 22-4-2026
Desc: Looping statements
"""
#natural nos print

'''num = int(input('Enter a number: '))
value = 1

while value <= num:
    print(value)
    value += 1'''

#armstrong number
num = input('Enter a number:')
count = len(num)
sum = 0

ni = int(num)
comp = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni // 10

if comp == sum:
    print('Armstrong Number')
else:
    print('Not an armstrong number')