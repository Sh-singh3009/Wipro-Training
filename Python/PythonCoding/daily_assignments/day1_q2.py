#Q2 Count how many times "a" appears in a string using enumerate.

str = str(input('Enter the string: '))
count = 0

for i, char in enumerate(str):
    if char == 'a':
        count += 1

print("The letter 'a' appears: ", count, "times")