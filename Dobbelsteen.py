from random import randint

die = 6
trigger = 1
run = True
points = 0

while run:
    inp = input("Wil je gooien j/n: ")
    if inp == "j" or inp == "J":
        roll = randint(1, die)
        if roll != trigger:
            points = points + roll
            print(roll.__str__() + " Punten zijn toegevoegd.")
            print("Jouw score is: " + points.__str__())
            
        else:
            run = False
            print("Jouw score is 1! Jouw score was: " + points.__str__())
    else: 
        run = False
        print("Jouw score is: " + points.__str__())
    