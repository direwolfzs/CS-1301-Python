"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
I did refer to this website for the taylorSwift problem though:
http://stackoverflow.com/questions/385325/dropping-trailing-0-from-floats
"""

import math

def square(base):
    b = int(base)**2
    return b


###########################################

def taylorSwift(numFans):
    fansTime = 3*numFans
    x = 9
    increment = float(fansTime) // 60
#changing minutes from 9:00 to 9:59
    if fansTime > 0:
       if fansTime < 60:
        if fansTime > 10:
            print("TSwizzle will be done by 9:" + str(fansTime) + ".")
        if fansTime < 10:
            print("TSwizzle will be done by 9:0" + str(fansTime) + ".")
#changing hours and minutes from 10:00 to 12:59
       elif increment < 4:
            hourIncrement = float(x) + float(increment)
            y = ("%.1f" % hourIncrement).replace(".0", "")
            properMinute = float(fansTime) % (60*float(increment))
            z = ("%.1f" % properMinute).replace(".0", "")
            if properMinute > 10:
                print("TSwizzle will be done by " + str(y) + ":" + str(z) + ".")
            else:
                print("TSwizzle will be done by " + str(y) + ":0" + str(z) + ".")
#changing the hours and minutes past 12:59 AM
       else:
        x=0
        incrementCut = float(increment) - 4
        g = incrementCut % 12
        hourIncrement = float(x) + float(g)
        y = ("%.1f" % hourIncrement).replace(".0", "")
        properMinute = float(fansTime) % (60*float(increment))
        z = ("%.1f" % properMinute).replace(".0", "")
        if properMinute > 10:
            print("TSwizzle will be done by " + str(y) + ":" + str(z) + ".")
        else:
            print("TSwizzle will be done by " + str(y) + ":0" + str(z) + ".")
#if there are no fans
    else:
     print("TSwizzle will be done after an incredibly busy day by 9:00.")
    return None


#################################################

def girlScoutCookies():
    x = input("How many boxes do you want?")
    y = input("How much money do you have?")
    z = float(x)*4
    a = float(y)-float(z)
    b = abs(a)
    print("You still need $" + str(b))


##################################################

def conversionTime(metersPerSecond):
    fps = metersPerSecond*3.28084
    mph = (3600 / 5280)* fps
    kph = (3600 / 1000)* metersPerSecond
    a = round(fps, 2)
    b = round(mph, 2)
    c = round(kph, 2)
    print("You have " + str(b) + " mph, " + str(a) + " feet per second, and " +
    str(c) + " kilometer per hour.")

###################################################

def tipCalculator():
    bill = input("How much was the bill?")
    tipPercent = input("What percent of that would you like to pay (write only the number)")
    anyCoupons = input("Do you have any coupons, and if so, how much is it in dollars?")


    realTipPercent = float(tipPercent) * .01
    tippedBill = float(bill) * float(realTipPercent)
    theTip = math.ceil(tippedBill)

    billAfterCoupon = float(bill) - float(anyCoupons)

    taxes = float(billAfterCoupon) * .08
    totalCost = float(taxes) + float(theTip) + float(billAfterCoupon)
    totalCost = "$%0.2f" % (totalCost)
    return totalCost

##################################################




def falafel(falafelBall, hummus, pitaBread):
    totalFalafelBalls = float(falafelBall)
    totalHummus = float(hummus)
    totalPitaBread = float(pitaBread)

    fb = float(totalFalafelBalls) // 6
    humm = float(totalHummus) // 2
    pita = float(totalPitaBread) // 1
    pita = ("%.1f" % pita).replace(".0", "")
    fb =  ("%.1f" % fb).replace(".0", "")
    if fb > 0 and humm > 0 and pita > 0:
        if fb <= pita and fb <= humm:
            print("With " + str(falafelBall) + " falafel balls, " + str(pitaBread) +
            " pitas, and " + str(hummus) + " hummus, you can make a maximum of " + str(fb) + " falafels.")
        elif pita <= fb and pita <= humm:
            print("With " + str(falafelBall) + " falafel balls, " + str(pitaBread) +
            " pitas, and " + str(hummus) + " hummus, you can make a maximum of " + str(pita) + " falafels.")
        elif humm <= fb and humm <= pita:
            print("With " + str(falafelBall) + " falafel balls, " + str(pitaBread) +
            " pitas, and " + str(hummus) + " hummus, you can make a maximum of " + str(pita) + " falafels.")
    else:
        print("I can make zero falafels.")

