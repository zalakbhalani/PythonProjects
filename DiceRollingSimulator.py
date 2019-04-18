import random

print("Welcome to Dice Rolling Simulator!")
print("==================================")
print("Rolling the Dice")
a = random.randint(1,6)
print(f"You got a {a} number")
out = "y"
while out == "y":
    out = input("You want to roll the Dice again ?(y/n) ")
    if out == "n":
        print("Thank you for playing")
        break
    print("Rolling the Dice again ")
    a = random.randint(1, 6)
    print(f"You got a {a} number")

