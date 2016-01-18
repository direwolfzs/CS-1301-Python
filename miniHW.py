"""Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
"""


from Myro import *
init()

"""
def celebration():
    turnRight(10,3)
    beep(.75, 800)
    forward(.75,.75)
    beep(.75,1000)
    backward(.75,.75)
    beep(.75, 800)
    forward(.75,.75)
    beep(.75, 1000)
    backward(.75,.75)
    beep(.75, 800)
    forward(.75,.75)
    beep(4, 1000)
"""


def avoidWalls():

    for time in timer(360):
        while getIR("left") == 0:
            turnLeft(.5,.5)
        while getIR("right") == 0:
            turnRight(.5,.5)
        while getIR() == 0:
            forward(.25,1)
        forward(1, 1)


avoidWalls()



