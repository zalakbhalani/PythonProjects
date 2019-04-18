import random

def convert_lst_to_str(s):
    movie = ""
    return (movie.join(s))

def convert_str_to_list(l):
    movie = []
    return list(l)

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

movie1 = "now you see me"
p = "_" * len(movie1)
list1 = []
for i in range(len(movie1)):
    if movie1[i] == " ":
        list1.append(i)
movie2 = convert_str_to_list(p)
for j in list1:
    movie2[j] = " "
movie3 = convert_lst_to_str(movie2)

print(movie3)
turns = 9
while turns:
    a = str(input("Enter word for the film: "))
    list2 = []
    if a in movie1:
        for i in range(len(movie1)):
            if movie1[i] == a:
                list2.append(i)
        movie2 = convert_str_to_list(movie3)
        for j in list2:
            movie2[j] = a
        movie3 = convert_lst_to_str(movie2)
        print(movie3,"\n")
        list2.clear()
        if movie3 == movie1:
            print("You won!!")
            break
    else:
        print("You guessed the wrong word")
        turns -= 1
        print("You have", + turns, 'more guesses')
        print(movie3,"\n")
if movie3 == movie1:
    print("You won!!")
else:
    print("You lost.")


