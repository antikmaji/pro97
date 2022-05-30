import random;


number=random.randint(1,9)

chances=0

while chances<=5:
    guess=int (input("Guess a number between 1 to 9"))

    


    if guess==number:

       print("Congratulations you WON!")
    
    elif guess<number:

        print("Guess is too low")

    else:

       print("Guess is too high")

    chances=chances+1

if chances==5:
    print("You Lost !")
