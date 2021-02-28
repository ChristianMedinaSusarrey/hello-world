import random
# 1 –FIND THE NUMBER
# Create a program invoked in the command line.
# It generatesa random number between 1 and 30(including 1 and 30).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. Keep the game going until the user types “exit”
# or find the number. Keep track of how many guesses the user has taken, and when the game ends,
# print them out on console and in a file named GuessingSteps.txt Name of the program: findNumber.py
randomNumber = random.randint(1, 30)
#print(randomNumber)
tryNumber = 0
print("Hello! Try to guess the generated random number")
guess =input("type a number to try to guess (exit to end the program):")
logs = "number to guess  for this run: " + str(randomNumber) + " \n"
winMessage = "Congrats!!!! you won on the attempt: "
tooLowMessage = "Sorry, too low, attempt: "
tooHighMessage = "Sorry too high attempt: "
while guess != "exit":
    guess = int(guess)
    #print("You said: " + guess)
    tryNumber += 1
    if guess == randomNumber:
        print(winMessage + str(tryNumber))
        logs += winMessage + str(tryNumber) + " user given number: " + str(guess) +"\n"
        guess = "exit"        
    elif guess < randomNumber:
        print(tooLowMessage + str(tryNumber))
        logs += tooLowMessage + str(tryNumber) + " user given number: " + str(guess) +"\n"
        guess =input("type a number to try to guess (exit to end the program):")
    else:
        print( tooHighMessage + str(tryNumber))
        logs += tooHighMessage + str(tryNumber) + " user given number: " + str(guess) +"\n"
        guess =input("type a number to try to guess (exit to end the program):")
else:
#   print("logs " + logs)
   print("Thanks for playing, number of tries: " + str(tryNumber))
   print(logs,  file=open('D:\\GuessingSteps.txt', 'w'))
   exit()


