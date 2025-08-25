import random

guess = random.randint(0,10)
print(guess)
while True:
    ask = int(input("Enter a number between 1-10 : "))
    if ask == guess:
        print(" Amazing , you are correct !")
        break
    elif ask<guess :
        print("too low")
    elif ask>guess:
        print("too high ")

