##########################################
# Guessing Game
##########################################

#Similar to the guessing game we played
#write a function guessing_game(), 
#it should run a loop that queries the user for inputs (guesses)
#compares each guess to a pre-set number between 0 and 10000
#and returns the new range
#as long as the correct answer is not inputted
#user is asked for guesses

#Each guess should work to reduce the range


#Hint: Break down the problem into smaller parts 
#and think about how to solve each part individually before
#thinking about combining them



##########################################
# Bonus Bonus
##########################################

#Make your function complain if the guess is less than 0 or greater than 10000


#have a while loop that works when X is NOT Guess then checks if guess greater than 0 or greater than 100
#if not then      
import random
guess = input("Take a guess anywhere between 0 and 1000: ")
def pain_and_suffering(guess):
    x = random.randint(0, 1000)
    z = 1000
    v = 0
    while int(guess) != x:
        if  (int(v)<int(x)<int(guess)) and 0 < int(guess) < 1000 :                
            z = guess
            guess = input("Take a guess anywhere between " + str(v) + " and "  + str(z) + "! " )
        elif (int(guess) < int(x) <int(z)) and 0 < int(guess) < 1000:
            v = guess
            guess = input("Take a guess anywhere between " + str(v) + " and " + str(z) + "! ")
        else:
            print ("Your number is out of the range please print a number between 1 and 1000.")
            guess = input("Take a guess anywhere between 0 and 1000: ")
    print ("You found the number. Good job!")

pain_and_suffering(guess)
