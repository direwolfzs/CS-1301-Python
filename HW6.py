"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
"""


from Myro import *
init()

def hw6():
    blueCount = 0
    redCount = 0
    verticalCount = 0
    horizontalCount = 0
    picture = takePicture()
    show(picture)

    for i in range(getWidth(picture)):
        for j in range(getHeight(picture)):
            pixel = getPixel(picture, i, j)

            #Looking for blue or red pixies
            bluePixel = getBlue(pixel)
            redPixel = getRed(pixel)
            if bluePixel > 30 and redPixel < 20 :
                blueCount += 1
            if redPixel > 50 and bluePixel < 35:
                redCount += 1


    #Checks if vertical or horizontal.
    for y in range(getHeight(picture)):
        a = getPixel(picture,20,y)
        bluePixel = getBlue(a)
        redPixel = getRed(a)
        if (bluePixel > 30 and redPixel < 20) or (redPixel > 50 and bluePixel < 35):
            setRGB(a, (0,0,0))
            verticalCount += 1


    for x in range(getWidth(picture)):
        c = getPixel(picture, x, 20)
        bluePixel = getBlue(c)
        redPixel = getRed(c)
        if (bluePixel > 30 and redPixel < 20) or (redPixel > 50 and bluePixel < 35):
            setRGB(c, (0,0,0))
            horizontalCount += 1

    print("redCount " + str(redCount))
    print("blueCount " + str(blueCount))
    print("isVerticalCount " + str(verticalCount))
    print("isHorizontalCount " + str(horizontalCount))
    show(picture)

    if verticalCount < horizontalCount:#vertical line
        forward(1,1)
        backward(1,1)

        if redCount > blueCount :#line is red
            beep(2,800)
        else:#line if blue
            beep(2,800)
            beep(2,0)
            beep(2,800)

    if horizontalCount < verticalCount:#horizontal line
        turnRight(1,5)
        turnLeft(1,5)

        if redCount > blueCount:#line is red
            beep(2,800)
        else:#line if blue
            beep(2,800)
            beep(2,0)
            beep(2,800)
    print("I did everything")

hw6()
