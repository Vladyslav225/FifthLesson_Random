import random

evenList = [ ]
oddList = [ ]

#Random distribution to the list of even and odd numbers
for i in range(100):

    value = random.randint(1, 100)
    # print(value)

    if value % 2 == 0:
        evenList.append(value)
        print(evenList)

    elif not value % 2 == 0:
        oddList.append(value)
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


