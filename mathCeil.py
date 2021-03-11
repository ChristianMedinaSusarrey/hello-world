#Given the math.ceil function,
# Define a set of unit test cases that exercise the function (Remember Right BICEP)
import math
import time

# Right
# Are results right?
print("RIGHT")
print(math.ceil(1.7))
print(math.ceil(7.2))
print(math.ceil(-4.9))
print(math.ceil(2.0))

#B
# Are all the boundary conditions CORRECT?
print("B")
print(math.ceil(1.9))
print(math.ceil(-4.9))
print(math.ceil(999999999.9999999999999999999999999))
print(math.ceil(-999999999.9999999999999999999999999))

#I
# CAN YOU CHECK INVERSE RELATIONSHIPS?
print("I")
Tup = (10.98, 20.26, 30.05, -40.95 , 50.45) # Tuple Declaration
Lis = [-10.98, 32.65, -39.59, -42.15 , 35.97] # List Declaration

print( math.ceil(math.pi))

print(math.ceil(5 + 3 - 1))



#C
# CAN YOU CROSS CHECK RESULTS USING OTHER MEANS?
print("C")

#E
# CAN YOU FORCE ERROR CONDITIONS TO HAPPEN?
print("E")
#print(math.ceil('Python'))

#P
# ARE PERFORMANCE CHARACTERISTICS WITHIN BOUNDS?
print("P")
# current date and time
start = time.time()

print(math.ceil(1.7))
print(math.ceil(7.2))
print(math.ceil(-4.9))
print(math.ceil(2.0))



Tup = (10.98, 20.26, 30.05, -40.95 , 50.45) 
Lis = [-10.98, 32.65, -39.59, -42.15 , 35.97] 
print(math.ceil(10))
print(math.ceil(-15))
print(math.ceil(Tup[2]))
print(math.ceil(Lis[2]))
end = time.time()
print(end - start)





