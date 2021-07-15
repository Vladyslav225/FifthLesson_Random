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

########

iterationCounter = 0

max_iterationCounter = 0

firstNumber = int(input(": "))
secondNumber = int(input(": "))



while max_iterationCounter < 1:

    firstNumber = random.uniform(firstNumber, secondNumber)
    secondNumber = random.uniform(firstNumber, secondNumber)

    print(firstNumber, secondNumber)

    if firstNumber == secondNumber:
        print(round(firstNumber, 2))
        print(round(secondNumber, 2))
        break

    iterationCounter +=1

#Number of iterations
print("The loop counter", iterationCounter, "times.")

#Calculation of repetition as a perxentage
print("{0:.2f}%".format(iterationCounter * 1 / 100))