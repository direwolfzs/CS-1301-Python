
"""Hasan Qadri, 903138378, hqadri6@gatech.edu, I worked on this assignment alone,
using only this semester's course materials.
for seconds in timer(60)
"""
"""
def avoidWalls():

    for x in range(timer(60)):
        while getIR() != 1 or getObstacle('center') == 0:
            forward(3,3)
            if getIR() == 1 or getObstacle('center') != 0:
                turnRight(1,100)
    celebration()

and getObstacle("left") == 0 and getObstacle("right") == 0:
"""


from Myro import *
init()

def celebration():
    beep(1, 800)
    beep(1,900)
    beep(3, 1000)
    beep(5, 500)
    beep(2, 200)
    beep(4, 500)

    beep(4, 2000)
    turn(4, 90)


def avoidWalls():

    for time in timer(60):
        while getIR("left") == 1 and getIR("right") == 1:
            backward(8, 1)

        forward(1,2)
        turnRight(1,1)
    celebration()
"""
        getObstacle("left") == 0 and getObstacle("right") == 0:
            forward(1,1)
        elif getIR() == 1:
            backward(5,1)
            turnRight(5, 1)
        elif getObstacle() != 0:
            turnRight(5,3)
            """


avoidWalls()
