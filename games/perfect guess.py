# Use of random package in python
# guess the number in minimum number of steps



import random

randomNo=random.randint(1,50)
guesses=0
userGuess= None
#print(randomNo)

while(userGuess!= randomNo):
    userGuess=int(input("Enter your Guess: "))
    guesses +=1
    if (userGuess==randomNo):
        print("You guessed right")
    else :
        if(userGuess < randomNo):
            print("You guessed it wrong!")
            print("Enter a larger number ")
        else:
            print("You guessed it wrong!")
            print("Enter a smaller number")
        

print(f"You guessed the number in : {guesses} guesses")


