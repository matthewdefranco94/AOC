#AOC Day 2

def importString():
    #Context manager 'with' , when this goes out of scope, free this up
    with open(r'C:\Users\Matthew\Desktop\AOC\2021\day2input2021.txt', 'r') as file:
        depthsMeasurements = file.read().splitlines()
        return depthsMeasurements

#forward = +horizontal
#down = +vertical
#up = -vertical

def movement():
    positionHorizontal = 0
    positionVertical = 0


    for x in importString():
        direction = x.split()[0]
        value = x.split()[1]
        if(direction == 'forward'):
            positionHorizontal += int(value)
        
        if(direction == 'up'):
            positionVertical -= int(value)
        
        if(direction == 'down'):
            positionVertical += int(value)
    
        endingValue = positionHorizontal*positionVertical

    return positionHorizontal, positionVertical, endingValue


def goldenAim():
    positionHorizontal = 0
    positionVertical = 0
    aim = 0
    endValue = 0

    for x in importString():
        direction = x.split()[0]
        value = x.split()[1]

        if(direction == 'forward'):
            positionHorizontal += int(value)
            positionVertical += aim * int(value)

        if(direction == 'down'):
            aim += int(value)

        if(direction == 'up'):
            aim -= int(value)

    endValue = positionVertical * positionHorizontal
    return endValue

print(goldenAim())
