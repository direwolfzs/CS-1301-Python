""" Hasan Qadri, A03, 903138378, hqadri6@gatech.edu,
I worked on the homework assignment alone, using only this semester's course materials. """

def machToFPS():
    """converting speeds in mach to feet per sec"""
    y = input("How fast are you going in mach? I'll convert that to fps for no reason at all.")
    mach = 1116.4370079
    theFPS = float(y) * mach
    print(str(theFPS) + " feet per second")


def sqPyramidVolume():
    """calculating volume of square pyramid"""
    x = input("Enter length of one side of the Egyptian pyramid base.")
    z = input("Enter hieght of the pyramid.")
    vol = ((float(x)**2)*float(z))/3
    print("The volume of the square pyramid is " + str(vol) + " inches-cubed.")


def makeChange():
    """Covnverting cents  to currency"""
    w = input("Yo, how many cents do you have?")
    dollars = (int(w) // 100)
    quarters = (float(w) % 100) // 25
    dimes = ((float(w) % 100) % 25) // 10
    nickels = (((float(w) % 100) % 25) % 10) // 5
    pennies = ((((float(w) % 100) % 25) % 10) % 5) // 1
    print("You have " + str(dollars) + " dollars, " + str(quarters) + " quarters, " + str(dimes) + " dimes, "
    + str(nickels) + " nickels, and " + str(pennies) + " pennies.")


def PPIIndex():
    """We are calculating a person's corrected PPI"""
    a = input("How fat are you, in pounds?")
    b = input("How close to the sky are you? (hieght in inches)")
    ppi = (float(a)/float(b))*1.125
    k = round(ppi,1)
    print("Your corrected PPI is " + str(k) + ".")

