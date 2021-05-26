# expenses must equal 2020
expenses = []

# r will ignore escape characters
with open(r'C:\Users\Matthew\Desktop\AOC\day1input.txt', 'r') as file:
    expenses = file.read().splitlines()

sumTarget = 2020
sum = 0
number1 = 0
number2 = 0
number3 = 0
prod = 0

for x in range(len(expenses) - 3):
    for y in range(x + 1, len(expenses) - 2):
        for z in range(y + 1 , len(expenses) - 1):
            number1 = int(expenses[x])
            number2 = int(expenses[y])
            number3 = int(expenses[z])

            #print("Number1: ", number1, " Number2: ", number2)
            sum = number1 + number2 + number3
            #print(sum)

            if sum == sumTarget:
                prod = number1 * number2 * number3

                print('Product of target sum found: ', number1, ' and ', number2, ' and ', number3)
                print(prod)
                break