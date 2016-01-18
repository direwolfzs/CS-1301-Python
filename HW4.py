"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
"""

from Myro import *
init()


def themeSong():
    beep(1, 800)
    beep(1, 800)
    beep(1,800)

    beep(1,1000)
    beep(1,1000)
    beep(1,1000)
    beep(1,800)
    beep(1, 800)
    beep(1, 800)
    beep(1, 600)
    beep(1, 600)
    beep(1, 600)
    beep(1, 800)
    beep(1, 500)
    beep(1, 400)
    beep(1, 300)

def secondAbility():    #avoid walls power
    for time in timer(10):
        while getIR("left") == 0:
            turnRight(1,1)
        while getIR("right") == 0:
            turnLeft(1,1)
        while getIR() == 0:
            forward(1,1)
        backward(1, 1)

def thirdAbility():     #The robot pretends he is dodging bullets
    for time in timer(10):
        forward(1,1)
        backward(1,1)
        turnRight(1,1)

def signatureAbility(): #robot performs whirlwind!
    themeSong()
    for time in timer(10):
        turnRight(90,1)
    z = getName()
    print(z)


def battleMenu():
    a = input("1. One Ability \n 2. Two Abilities  \n 3. Three Abilities  \n 4. Exit")
    while float(a)!=1 and float(a)!=2 and float(a)!=3 and float(a)!=4:
        print("Sorry, invalid choice.")
        a = input("1. One Ability \n 2. Two Abilities  \n 3. Three Abilities  \n 4. Exit")
    while float(a) ==2 or float(a) ==3 or float(a)==1:
        if float(a)==1:
            signatureAbility()
            a = input("1. One Ability \n 2. Two Abilities  \n 3. Three Abilities  \n 4. Exit")
        elif float(a)==2:
            signatureAbility()
            secondAbility()
            a = input("1. One Ability \n 2. Two Abilities  \n 3. Three Abilities  \n 4. Exit")

        elif float(a)==3:
            signatureAbility()
            secondAbility()
            thirdAbility()
            a = input("1. One Ability \n 2. Two Abilities  \n 3. Three Abilities  \n 4. Exit")

    else:
        print("By exiting, you have failed not only the city, but also your aging mother. \n For shame, good sir, for shame. \n Oh wait. According to the instructions, if you press \n exit, you won the battle. Congratz.")



battleMenu()