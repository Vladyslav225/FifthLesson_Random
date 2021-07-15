import random

evenList = [ ]
oddList = [ ]

#Random distribution to the list of even and odd numbers
for valueRandint in range(100):

    valueRandint = random.randint(1, 100)
    # print(value)

    if valueRandint % 2 == 0:
        evenList.append(valueRandint)
        print(evenList)

    elif not valueRandint % 2 == 0:
        oddList.append(valueRandint)
        print(oddList)

#The sum of the even list
sum_evenList = sum(evenList)
print(sum_evenList)


#The sum of the odd list
sum_oddList = sum(oddList)
print(sum_oddList)


#Convert to dictionary
lists = [
    ["Even_List", evenList],
    ["Odd_List", oddList],
    ["Sum_Even_List", sum_evenList],
    ["Sum_Odd_List", sum_oddList]
]

objects = dict(lists)
print(objects)


loopCounter = 0


firstNumber = int(input(": "))
secondNumber = int(input(": "))

while True:

    firstNumber = random.uniform(firstNumber, secondNumber)
    secondNumber = random.uniform(firstNumber, secondNumber)

    print(round(firstNumber, 2))
    print(round(secondNumber, 2))

    if firstNumber == secondNumber:
        print(firstNumber, secondNumber)
        break

    loopCounter +=1

    break

print("The loop counter", loopCounter, "times.")