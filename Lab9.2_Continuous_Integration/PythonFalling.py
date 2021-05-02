# You need to create two functions to substitute str() and int(). 
# A function called int_to_str() that converts integers into strings 
# and a function called str_to_int() that converts strings into integers

#The ord() function returns an integer representing the Unicode character.
import re

def int_to_str(num, base=10):
    if num // base == 0:
        return chr(num + ord('0'))
    return int_to_str(num // base, base) + chr(num % base + ord('0'))


def str_to_int(s):
    rtr=0
    for c in s:
        rtr=rtr*10 + ord(c) - ord('0')
    return rtr 

def isNegative(numInt):
    isNegativeFlag = False
    if numInt<0:
        numInt = numInt * -1
        isNegativeFlag = True
    return isNegativeFlag
    

numString = "100"
numInt = 300
negativeFlag = False

negativeFlag = isNegative(numInt)

if "-" in numString:
    numString = re.sub('-', '', numString)
    negativeFlag = True
print("******* str_to_int  ********")
numString2 = str_to_int(numString)
print(type(numString2))
if negativeFlag:
    print(numString2 * -1)
else:
    print(numString2)

print("****** int_to_str *********")
numInt2 = int_to_str(numInt)
print(type(numInt2))
if negativeFlag:
    print("-" + numInt2)
else:
    print(numInt2)
