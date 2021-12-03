#AOC Day 3

#powerConsumption = gamma * epsilon
#gamma rate
#epsilon rate

def importString():
    #Context manager 'with' , when this goes out of scope, free this up
    with open(r'C:\Users\Matthew\Desktop\AOC\2021\day3input2021.txt', 'r') as file:
        depthsMeasurements = file.read().splitlines()
        return depthsMeasurements

#fixedList = [int(i) for i in importString()]

#going by y and getting the x element[first element]
#12345
#12345
#12345

#distance = 12

list = importString()

def gamma():
    number = ""
    ones = 0
    zeroes = 0


    for y in range(12):
        for x in list:
            if(x[y] == "1"):
                ones += 1
            if(x[y] == "0"):
                zeroes +=1
        if (ones > zeroes):
            number+=("1")
        else:
            number+=("0")
        zeroes = 0
        ones = 0
    return int(number,2)

def epsilon():
    number = ""
    ones = 0
    zeroes = 0

    for y in range(12):
        for x in list:
            if(x[y] == "1"):
                ones += 1
            if(x[y] == "0"):
                zeroes +=1
        if (ones < zeroes):
            number+=("1")
        else:
            number+=("0")
        zeroes = 0
        ones = 0
    return int(number,2)

def consumption():
    return epsilon() * gamma()




print(epsilon())
print(gamma())
print(consumption())








