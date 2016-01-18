
"""
Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials
"""
from Myro import *


def seeingRed():  #15 points
    pic = takePicture()
    savePicture(pic, "seeingRedOriginal.png")
    show(pic)
    for pixel in getPixels(pic):
        a = getRed(pixel)
        a = 255
        setRed(pixel, a)

    seeingRed = savePicture(pic, "seeingRedProcessed.png")

def seeingBlue():  #15 points
    pic = takePicture()
    savePicture(pic, "seeingBlueOriginal.png")
    show(pic)
    for pixel in getPixels(pic):
        a = getBlue(pixel)
        a = 255
        setBlue(pixel, a)
    savePicture(pic, "seeingBlueProcessed.png")


def seeingGreen():  #15 points
    pic = takePicture()
    savePicture(pic, "seeingGreenOriginal.png")
    show(pic)
    for pixel in getPixels(pic):
        a = getGreen(pixel)
        a = 255
        setGreen(pixel, a)
    savePicture(pic, "seeingGreenProcessed.png")

def seeingCyan():  #15 points
    pic = takePicture()
    savePicture(pic, "seeingCyanOriginal.png")
    show(pic)
    for pixel in getPixels(pic):
        a = getBlue(pixel)
        a = 255
        setBlue(pixel, a)
        b = getGreen(pixel)
        b = 255
        setGreen(pixel, b)
    savePicture(pic, "seeingCyanProcessed.png")


def seeingMagenta():  #15 points
    pic = takePicture()
    savePicture(pic, "seeingMagentaOriginal.png")
    show(pic)
    for pixel in getPixels(pic):
        a = getRed(pixel)
        a = 255
        setRed(pixel, a)
        b = getBlue(pixel)
        b = 255
        setBlue(pixel, b)
    savePicture(pic, "seeingMagentaProcessed.png")


def splitScreen(): #50 Points
    pic = takePicture()
    aList = []
    x  =0
    while x < 2:
        turnRight(1,1)
        pic1 = takePicture()
        savePicture(pic1, "Splitscreenhalf1.png")
        print("pic 1 now")

        heightPicOne = getHeight(pic1) // 2
        turnRight(1,1)
        pic2 = takePicture()
        savePicture(pic2, "Splitscreenhalf2.png")
        print("pic 2 now")
        heightPicTwo = getHeight(pic2)// 2

        for i in range(getWidth(pic)):
            for j in range(heightPicOne):
                #setColor(getPixel(pic1, i, j), getColor(getPixel(pic, i, j)))
                pixel1 = getPixel(pic1, i, j)
                pixel2 = getPixel(pic, i, j)
                setRed(pixel2, getRed(pixel1))
                setBlue(pixel2, getBlue(pixel1))
                setGreen(pixel2, getGreen(pixel1))

        for i in range(getWidth(pic)):
            for j in range(heightPicOne, getHeight(pic)):
                #setColor(getPixel(pic2, i, j), getColor(getPixel(pic,i,j)))
                pixel1 = getPixel(pic2, i, j)
                pixel2 = getPixel(pic, i, j)
                setRed(pixel2, getRed(pixel1))
                setBlue(pixel2, getBlue(pixel1))
                setGreen(pixel2, getGreen(pixel1))

        print("pic processed")
        aList.append(copyPicture(pic))
        x = x+1
    savePicture(aList, "SplitscreenProcessed.gif")

def greenScreen():
    dark_forest = loadPicture("dark_forest.jpg")
    pic = loadPicture("testing.jpg")
    show(pic)
    for i in range(getWidth(pic)):
        for j in range(getHeight(pic)):
            pixel = getPixel(pic, i, j)
            pixel2 = getPixel(dark_forest, i, j)
            if getRed(pixel) > 170: #and getGreen(pixel) < 210 and getRed < 135 and getRed > 130:
                setRed(pixel, getRed(pixel2))
                setBlue(pixel, getBlue(pixel2))
                setGreen(pixel, getGreen(pixel2))
    savePicture(pic, "greenScreenPic.png")

greenScreen()

"""

def screenShake():
    pic = takePicture()

"""


def colorNegative(): #35 points, color negative of the picture GIF
    pic = takePicture()
    savePicture(pic, "colorNegativeOriginal.png")
    show(pic)
    aList = []
    z=0
    while z < 2:
        for pixel in getPixels(pic):
            setRed(pixel, 255- getRed(pixel))
            setBlue(pixel, 255- getBlue(pixel))
            setGreen(pixel, 255- getGreen(pixel))
        aList.append(copyPicture(pic))
        turnLeft(1,1)
        pic = takePicture()
        savePicture(pic, "colorNegativeOriginal2.png")
        z = z+1

    savePicture(aList, "colorNegativeProcessed.gif")


def multipleExposure(): #50 points
    z=0
    pic1 = takePicture()
    savePicture(pic1, "multipleExposureOriginal1.png")
    show(pic1)
    pic2 = takePicture()
    savePicture(pic2, "multipleExposureOriginal2.png")
    show(pic2)
    pic3 = takePicture()
    savePicture(pic3, "multipleExposureOriginal3.png")
    show(pic3)
    while z< 1:
        for x in range(getWidth(pic1)):
            for y in range(getHeight(pic1)):
                r1, g1, b1 = getRGB(getPixel(pic1, x, y))
                r2, g2, b2 = getRGB(getPixel(pic2, x, y))
                r3, g3, b3 = getRGB(getPixel(pic3, x, y))

                rAverage = (r3+r2+r1)/3
                bAverage = (b1+b2+b3)/3
                gAverage = (g1+g2+g3)/3

                setRed(getPixel(pic3, x, y), rAverage)
                setBlue(getPixel(pic3, x, y), bAverage)
                setGreen(getPixel(pic3, x, y), gAverage)
        z = z+1

    multipleExposure = savePicture(pic3, "multipleExposureProcessed.png")



def fade():  #35 points
    pic = takePicture()
    show(pic)
    aList = []
    z = 50
     #Looks at all red, green, blue pixels, decreases the tint down to black

    while getRed(pixel) >= 50 or getBlue(pixel) >= 50 or getGreen(pixel) >= 50:
        for pixel in getPixels(pic):
            a = getRed(pixel)
            if a > 50:
                setRed(pixel, a-z)
            else:
                set(pixel, 0)

            b = getBlue(pixel)
            if b > 50:
                setRed(pixel, b-z)
            else:
                set(pixel, 0)

            c = getGreen(pixel)
            if c > 50:
                setRed(pixel, c-z)
            else:
                set(pixel, 0)

            aList.append(copyPicture(pic))


        pic = takePicture
        z= z+50

    savePicture(aList, "fadePicture.gif")
