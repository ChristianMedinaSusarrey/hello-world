# Given the filecmp.cmp function,
# Define a set of test cases that exercise the function (Remember Right BICEP)

import time
import filecmp
import os


# Path 01
file1 = "C:\\Users\\chris\\Desktop\\test01.txt"
# Path 02
file2 = "C:\\Users\\chris\\Desktop\\test02.txt"
   
comp = filecmp.cmp(file1, file2, shallow = False) 


# Right
# Are results right?
print("RIGHT")


print(filecmp.cmp(file1, file2, shallow = False) )
print(filecmp.cmp(file2, file1, shallow = False) )
print(filecmp.cmp(file1, file1, shallow = False) )

#B
# Are all the boundary conditions CORRECT?
print("B")
#long path
file1 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\Test\\Test\\Test\\Test\\Test\\Test\\Test\Test01\\test01.txt"
file2 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\Test\\Test\\Test\\Test\\Test\\Test\\Test\Test02\\test02.txt"
print(filecmp.cmp(file1, file2, shallow = False) )
#long path and text name
file1 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test01\\test0000000000000000000000000000000000000000000000000000000000000001.txt"
file2 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test02\\test0000000000000000000000000000000000000000000000000000000000000002.txt"
print(filecmp.cmp(file1, file2, shallow = False) )

#a lot of content in files
file1 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test01\\A01.txt"
file2 = "C:\\Users\\chris\\Desktop\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test\\Test02\\B02.txt"
print(filecmp.cmp(file1, file2, shallow = False) )

#I
# CAN YOU CHECK INVERSE RELATIONSHIPS?
print("I")


#C
# CAN YOU CROSS CHECK RESULTS USING OTHER MEANS?
print("C")

path01 = "C:\\Users\\chris\\Desktop\\test01.txt"
path02 = "C:\\Users\\chris\\Desktop\\test01.txt"

f = open(path01, "r")
f.close()

f2 = open(path02, "r")
f2.close()

if path01 == path02:
    print("paths are equal")

print(filecmp.cmp(file1, file2))

path01 = "C:\\Users\\chris\\Desktop\\test01.txt"
path02 = "C:\\Users\\chris\\Desktop\\test02.txt"

f = open(path01, "r")
f.close()

f2 = open(path02, "r")
f2.close()

if path01 != path02:
    print("paths are NOT equal")
print(filecmp.cmp(file1, file2))






#E
# CAN YOU FORCE ERROR CONDITIONS TO HAPPEN?
print("E")

path01 = "C:\\Users\\chris\\Desktop\\thisFileDoesntExist01.txt"
path02 = "C:\\Users\\chris\\Desktop\\thisFileDoesntExist02.txt"
# print("Next Line should trigger FileNotFoundError")
# print(filecmp.cmp(path01, path02))

#P
# ARE PERFORMANCE CHARACTERISTICS WITHIN BOUNDS?
print("P")
# current date and time
start = time.time()






end = time.time()
print(end - start)