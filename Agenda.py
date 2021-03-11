# Implement a class that manages a directory
# that is saved in a text file.
# The data saved includes:a.Name b.Email c.Age d.Country of Origin
# The class should have capabilities to:
# -Add new record
# -Delete a record
# -Look for a record by mail and age
# -List on screen all record information
import fileinput
import time
import os

class Person:
 def __init__(self, name, email, age, country):
    self.name = name
    self.email = email
    self.age = age
    self.country = country

 def addPerson(self):
     record =  self.name + "," + self.email + "," + self.age + "," + self.country
     #f = open(record, "D:\\myAgenda.txt", "w")  
     print(record,  file=open('D:\\myAgenda.txt', 'a'))
 def getAllRecords(self):
     with open('D:\\myAgenda.txt', 'r') as f:
      print(f.read())
 def searchRecord(self,search): 
     #search = input("Search: ")        
     fiIn = open('D:\\myAgenda.txt').readlines()     
     for lines in fiIn:
         if search in lines:
             print (lines)
         #else:
             #print ("Nothing found! " + lines)
 def toDelete(self,toDelete): 
     #toDelete = input("Which contact would you like to delete?")
     with fileinput.FileInput("D:\\myAgenda.txt", inplace=True, backup='.bak') as file:
          for line in file:            
             if toDelete in line:
                 line = ''
             else:
                 print(line)             


print("Hello!")
print("Type an action to start!")
print("1: Add Contact")
print("2: Delete")
print("3: Search by email or age")
print("4: Return all records")
option =input(": ")
p1 = Person("","","", "")

if option == '1':
    # Do the thing
    print("Adding a new contact... ")
    name =input("Name: ")
    email =input("Email: ")
    age =input("Age: ")
    country =input("Country: ")   
    p1 = Person(name,email,age,country)
    p1.addPerson()
    p1.getAllRecords()
elif option == '2':
    # Delete a contact
    print("Delete a contact")
    toDelete = input("Which contact would you like to delete?")
    p1.toDelete(toDelete)
    
elif option == '3':
    # Search by email or age
    print("Search by email or age. Please provide a value to search for: ") 
    search = input("Search: ")       
    p1.searchRecord(search)
elif option == '4':
    # Get All Records
    print("Get all records")
   
    p1.getAllRecords()
else:
    # Do the default
    print("No valid option selected, please try again.")


#Performance variable related
start = time.time()
# Right Bicep
# RIGHT
# Verify adding is working
name = "Christian"
p1 = Person(name,"christian@tec.mx","25","MX")
p1.addPerson()
p1.searchRecord(name)
p1.toDelete(name)
# To verify all functions work as expected (add, delete and search)
# B
# Are all the boundary conditions CORRECT?
longName = "This is a very very very long name"
longEmail = "This is a very very very long email without email format"
age = "This isnt even a number" #TODO validate data type
country = "NotACountry" #TODO get a list of valid entries here, maybe?
p1 = Person(name,longEmail,age,country)
p1.addPerson()
p1.searchRecord(longName)
p1.searchRecord(longEmail)
p1.toDelete(longEmail)
# I
# CAN YOU CHECK INVERSE RELATIONSHIPS?

# Try to test without a file
# content = open('D:\\myAgenda.txt', 'a')
# if not content:

# Verify once the file is corrupted, updated with a different name or lost
# open('D:\\myAgenda.txt', 'a')


# C
# CAN YOU CROSS CHECK RESULTS USING OTHER MEANS?
#Search for an already deleted record, it shouldnt show
p1.searchRecord(longEmail)

#

# E
# CAN YOU FORCE ERROR CONDITIONS TO HAPPEN?
# access file while open
# open('D:\\myAgenda.txt', 'a')  Force to fail once file is open
p1.addPerson()
# Force to fail once two or more process are trying to get the same file resource
# Agenda()
# Test for at least supporting 1 GB file
# size = os.path.getsize("D:\\hugeAgendaFile.txt")
size = os.path.getsize("D:\\myAgenda.txt")
print("File size: " + str(size) + "bytes")
#

# Force an error while trying to write from multiple instances on the file, and verify if some of the content got lost

# P
# ARE PERFORMANCE CHARACTERISTICS WITHIN BOUNDS?
end = time.time()
print(end - start)