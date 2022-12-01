import sys

with open("input.txt", "r") as inputtxt:
    itemList = inputtxt.read().splitlines()

mostCalories = []
temp = 0

for item in itemList:
    if item == "":
        mostCalories = mostCalories + [temp]
        temp = 0
    else:        
        temp = temp + int(item)
    

mostCalories = sorted(mostCalories, reverse = True)[:3]

mostCaloriesSum = 0

for i in mostCalories:
    mostCaloriesSum += i
    
print(mostCaloriesSum)
