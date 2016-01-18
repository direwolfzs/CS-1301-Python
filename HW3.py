
"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.

"""

def applyToTech(reading, math, writing):
    a = "Congratulations, you have been admitted to Georgia Tech. Go Jackets!"
    b = "I am sorry to inform you we cannot offer you admission to Georgia Tech."
    c = "Invalid scores. Try again."
    if reading <= 800 and math <= 800 and writing <= 800:
        if reading >= 680 and math >= 690 and writing >=650:
                return a
        else:
                return b
    else:
        return c



################################

def guessAge(age):
    a = input("While walking through the woods, you \n stumbled through a portal and found \n an old man precariously  perched on top of a\n stump in a clearing. \n He blurts: 'Guess my age!' \n Perhaps you should play along")
    a = str(a)
    a = a.lower()
    if a != str("quit"):
        a = float(a)
        age = float(age)

        if a != age:
            b = input("Second try, guess my age!")
            b = str(b)
            b = b.lower()
            if b != str("quit"):
                b = float(b)
                if b != age:

                    c = input("Third try, guess my age!")
                    c = str(c)
                    c = c.lower()
                    if c != str("quit"):
                        c = float(c)
                        if c != age:

                            d = input("Fourth try, guess my age!")
                            d = str(d)
                            d = d.lower()
                            if d != str("quit"):
                                d = float(d)
                                if d != age:

                                    e = input("Fifth try, guess my age!")
                                    e = str(e)
                                    e = e.lower()
                                    if e != str("quit"):
                                        e = float(e)
                                        if e != age:

                                            f = input("Sixth and final try, guess my age!")
                                            f = str(f)
                                            f = f.lower()
                                            if f != str("quit"):
                                                f = float(f)
                                                if f != age:
                                                    x = a
                                                    while x ==a:
                                                        print("Thank you for playing, youngster.")
                                                        x = b

                                                else:
                                                    print("Great job! It took you 6 tries to guess the age.")
                                                    print("Thank you for playing.")
                                            else:
                                                print("Don't give up just because things are hard!")
                                        else:
                                            print("Great job! It took you 5 tries to guess the age.")
                                            print("Thank you for playing.")
                                    else:
                                        print("Don't give up just because things are hard!")
                                else:
                                    print("Great job! It took you 4 tries to guess the age.")
                                    print("Thank you for playing.")
                            else:
                                print("Don't give up just because things are hard!")
                        else:
                            print("Great job! It took you 3 tries to guess the age.")
                            print("Thank you for playing.")
                    else:
                        print("Don't give up just because things are hard!")
                else:
                    print("Great job! It took you 2 tries to guess the age.")
                    print("Thank you for playing.")
            else:
                print("Don't give up just because things are hard!")
        else:
            print("Great job! It took you 1 try to guess the age.")
            print("Thank you for playing.")
    else:
        print("Don't give up just because things are hard!")

####################################


def encryptMessage(secretMsg):
    theMessage = ""
    pos = 0
    while pos < len(secretMsg):
        letter = secretMsg[pos]
        if letter.isupper() and letter.isalpha():
            theMessage = theMessage + letter.lower() + "^"
        elif letter.isalpha():
            theMessage = theMessage + letter
        elif float(letter) == 1:
            theMessage = theMessage + "@"
        elif float(letter) == 2:
            theMessage = theMessage + "#"
        elif float(letter) == 3:
            theMessage = theMessage + "$"
        else:
            theMessage = theMessage + "*"

        pos = pos + 1

    print(theMessage)

####################################  seconds = "" minutes =""  hours = ""  "{1}:{0}:{2}".format(minutes, secnds, hours)
def numberPyramid(num):
    space = ""
    for y in range(num, 0, -1):  #iterates from 9-2
        print("{:}".format(y)*num+ "{}".format(space)+"{}".format(y)*num)
        num = num -1
        space = space + "  "

#######################################

def reverseMultiTable(n):
    for x in range(n, 0 , -1):
        for y in range(n, 0 , -1):
            multi = x*y
            if multi < 10:
                print(" " + str(multi), end=" ")
            else:
                print(x*y, end = " ")
        print()  #for new line



########################################3

def enoughFor():
    x = input("What letter-grade would you like to dream about?")
    x = x.lower()
    x = str(x)
    if str(x) != "a" and str(x)!= "b" and str(x)!= "c" and str(x)!= "d":
        print("Learn to read plz, I said letter-grade only.")
    else:
        if x == "a":
            x = 90
        if x == "b":
            x = 80
        if x == "c":
            x = 70
        if x == "d":
            x = 60
        y = input("How badly are you failing (current numeric grade)?")

        z = input("How much is your only hope worth(the final)?")

        finalExamGrade = (100 * float(x) - (100-float(z)) * float(y))/float(z)
        if x == 90:
            x = "A"
        if x == 80:
            x = "B"
        if x == 70:
            x = "C"
        if x == 60:
            x = "D"
        if finalExamGrade > 100 or finalExamGrade < 0:
            print("Its impossible for you to get this grade, Im sorry there is no hope for you.")
        else:
            print("You need " + str(finalExamGrade) + " in the final to get a(n) " + str(x) + " in the class.")

