import random

print("Guess Between The <1 - 10>")
number = random.randint(1 , 10)

while True:
    guess = input("Enter Your Guess Number : ")
    try :
        if int(guess) > number :
            print("Higher Guess ...")
        elif int(guess) < number :
            print("Lower Guess ...")
        else :
            print(f"You Win , Guess : {number}")
            break
    except ValueError:
        print("Please Enter Number !!" )