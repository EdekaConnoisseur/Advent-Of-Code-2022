import sys

with open("input.txt", "r") as inputtxt:
    itemList = inputtxt.read().splitlines()

mostCalories = 0
temp = 0

for item in itemList:
    if item == "":
        if mostCalories < temp:
            mostCalories = temp
        temp = 0
    else:        
        temp = temp + int(item)

print(mostCalories)
