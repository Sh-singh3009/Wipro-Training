
import re

#beg & end match
'''txt = input('Enter a text ')    #India is my country
bpat = input('Enter a beginning patter ')   #India
epat = input('Enter ending pattern ')    #country
bpat = '^' + bpat   #^India
epat = epat + '$'   #try$

if re.search(pattern=bpat, string=txt):
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=epat, string=txt):
    print('Ending pattern available')
else:
    print('Ending pattern not available')'''

#digit
'''mbno = input('Enter a mobile no ')
pat = r"/d"

if re.fullmatch(pattern=pat, string=mbno):
    print('only digits')
else:
    print('Other characters are available')'''

#username
'''un = input('Enter username ')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('Valid username')
else:
    print('Invalid username')'''

#email
'''emailadd = input('Email ')
#pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=emailadd):
    print('Valid email id')
else:
    print('Invalid email id')'''

#identifying pswd
'''pwdtxt = input('Enter password ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"

if re.match(pattern=pat, string=pwdtxt):
    print('Valid password')
else:
    print('Invalid password')'''

txt = input('Text ')
pat = r"\s+"

#sub substitutes the character
#print(re.sub(pattern=pat, string=txt, repl='*'))

print(re.split(pattern=pat, string=txt))