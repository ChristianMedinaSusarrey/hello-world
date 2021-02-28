# Create a program that parses a file given
# as parameter and counts the number of
# occurrences for a list of words identified
# in the file. The identification is sensitive
# case. The program will accept the words
# to test as arguments. English or Spanish.
# Name of the program: findWords.py

with open('Fuerza Natural - Cerati.txt', 'r') as file:
     data = file.read().replace('\n', ' ')
with open('Fuerza Natural - Cerati.txt') as file:
    fLine = file.readline()
    #To remove \n special character
    fLine = fLine.rstrip() 
    wordsToFind = fLine.split(',')
    wordsInText = data.split(' ')
    
#    print(wordsToFind)
#    print(wordsInText)
for i in range(len(wordsToFind)):
     count = 0
     print("Word " + wordsToFind[i])
     for j in range(len(wordsInText)):
      if wordsToFind[i] == wordsInText[j]:
       count = count + 1
     print("exists: " + str(count) + " times ")