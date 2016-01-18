""" Hasan Qadri, A03, 903138378, hqadri6@gatech.edu,
I worked on the homework assignment alone, using only this semester's course materials. """


def machToFPS(machList):
    """converting speeds in mach to feet per sec"""
    newList = map(lambda x: x * 1116.4370079, machList)
    print(newList)
    print(machList)
    x=0
    while x < len(machList):
        print(str(machList[x]) + " mach is equal to " + str(newList[x]))
        x = x+1

def sqPyramidVolume(baseHeightList, volumeList):
    """calculating volume of square pyramid"""
    newList = map(lambda x: ((x[0]**2)*x[1])/3, baseHeightList)
    correctList = filter(lambda x: x in volumeList, newList)
    return correctList

def makeChange(changeList):
    """Covnverting cents  to currency"""
    newList = []
    newList.append(changeList[0] * 100)
    newList.append(changeList[1]*25)
    newList.append(changeList[2] *10)
    newList.append(changeList[3]*5)
    newList.append(changeList[4]*1)
    totalValue = reduce(lambda x,y: x+y, newList)
    return totalValue

