import random

def Game():
    global tries
    Target_Number = random.randint(0, 100)
    while True:
        tries += 1
        try:
            User_Number = int(input("Guess a number from 1->100: "))
        except ValueError:
            print("Please enter a number")
        else:
            if User_Number < Target_Number:
                print("Pick a bigger number")
            elif User_Number > Target_Number:
                print("Pick a smaller number")
            else:
                print("You've won!!!")
                print(f"The number is indeed: {Target_Number}")
                print(f"you've won in {tries} tries")
                break


def No_Game():
    print("Alright then goodbye?")
    exit()

def Invalid_Input(): 
    print("Invalid Input")
    

while True:
    tries = 0
    match input("Do you want to play the guessing game?(y/n): "):
        case "y":
            Game()
        case "n":
            No_Game()
        case _:
            Invalid_Input()

