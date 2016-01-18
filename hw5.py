"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
"""
from Myro import*
init()


def onlySixths(listing):
    anArray = []
    for x in listing:
        if x%6 ==0:
            anArray.append(x)
    return anArray



def union(listing1, listing2):
    anArray = []
    theArray = []
    z = 0
    for x in listing1:
        anArray.append(x)
    for y in listing2:
        anArray.append(y)
    while z < len(anArray):
        theArray.append(min(anArray))
        anArray.remove(min(anArray))
    t = set(theArray)
    return t


def multiplyNums(listing):
    y = 0
    a=1
    z=1
    k=1
    for x in listing:
        if isinstance(x, int) or isinstance(x, float):
            a = a*x
        elif isinstance(x,str):
            k=k+1
        else:
            while y<len(x):

                z = z*x[y]
                y= y+1
    return a*z


def abbreviator(hangman):
    stringer = ""
    for x in hangman:
        if x.isalpha():
            if x.isupper():
                stringer = stringer + x
        elif x.isdigit():
            stringer = stringer +x
    return stringer



def parse(stringer, delimiter):
    anArray = []
    mordor = []
    word = ""
    for x in stringer:
        if x != delimiter:
            word = word + x
        else:
            mordor.append(x)
            anArray.append(word)
            word=""
    if word != "":
        anArray.append(word)
    return anArray



def lightStats():
    c = getLight()
    print("Left: " + str(c[0]) + "\nCenter: " + str(c[2]) + "\nRight: " + str(c[1]))

    mean = sum(c) / len(c)
    c = sorted(c)
    median = c[1]
    ranger = c[2] - c[0]
    c = [mean, median, ranger]
    return c


