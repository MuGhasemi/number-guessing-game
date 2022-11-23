import random

print("Guess Between The <1 - 10>")
number = random.randint(1 , 10)

while True:
    guess = input("-Enter Your Guess Number : ")
    try :
        if int(guess) > 10 or int(guess) <= 0:
            print("Please Enter Number Between <1 - 10>")
        elif int(guess) > number :
            print("Higher Guess ...")
        elif int(guess) < number :
            print("Lower Guess ...")
        else :
            print(f"You Win , Guess : {number}")
            guess = input("-Would You Like Try Again (yes or no)?  ")
            if guess == "yes" or guess == "y" :
                number = random.randint(1 , 10)
            elif guess == "no" or guess == "n":
                break
    except ValueError:
        print("Please Enter Number !!" )