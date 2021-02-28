# Create a command line program that take as input parameter a number and
# then it displays in the console the corresponding number (positive integers
# Plus Zero) in Binary and Hexadecimal. It also manages errors using exceptions for not using numbers.
# Covert the number using the algorithm and not a function. Name of the program: convert2X.py0
binaryNumber = ""
hexRep = ""
try:
   num = int(input("Number: "))
   hexNum = num
   if num == 0:
       binaryNumber = "0"
       hexRep = "0"
   while num > 0:
        binaryNumber += str(num % 2)
        num = num//2
   else:
    binaryNumber = binaryNumber[::-1]
    print("Binary " + binaryNumber)
   while hexNum>0:
       value = str (hexNum % 16 )
       hexNum = hexNum//16
       if value == '10':
        value = "A"
       if value == '11':
        value = "B"
       if value == '12':
            value = "C"
       if value == '13':
        value = "D"
       if value == '14':
        value = "E"
       if value == '15':
        value = "F"
       hexRep += str(value)
   else:
        hexRep = hexRep[::-1]
        print("Hex Represenation: " + hexRep)        
except ValueError:
   print("Please enter only positive integers plus Zero")
