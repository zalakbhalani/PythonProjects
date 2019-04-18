import random

number = random.randint(1,100)
user_number = 0
while user_number != number:
    user_number = int(input("Enter any integer number between 1 to 100: "))
    if user_number == number:
        print("HURREEE!!! You guessed the correct number")
    elif user_number > number:
        print("Your number is greater")
    else:
        print("Your number is lesser")



