#Advent of Code Day 1


def testOutput():
    SlidingGlassDoor(importString())


def importString():
    with open(r'C:\Users\Matthew\Desktop\AOC\day1input2021.txt', 'r') as file:
        depthsMeasurements = file.read().splitlines()
    return depthsMeasurements

def incrimenter(dataM):
    NumberofIncreases = 0
    for x in range(len(dataM)-1):
        if int(dataM[x+1]) > int(dataM[x]):
            NumberofIncreases += 1

#takes 3 elements of list, sums them, then moves over +1 in the list and compares the 2 list sums
def SlidingGlassDoor(compiledList):

    fixedList = [int(i) for i in compiledList]
    windowSize = 3    
    increasesAgain = 0
    for x in range(len(compiledList) - windowSize):

        firstwindowsum = sum(fixedList[x : x + windowSize])
        secondWin = sum(fixedList[x+1: x+ windowSize+1])

        if secondWin > firstwindowsum:
            increasesAgain += 1
            print(increasesAgain)

testOutput()