#Use of While loop, user input, integers

total = 0
count = 0

while total <= 45:
    num = int(input("Please enter a integer to add: "))
    total += num
    count += 1
    print("Number =", num)
    print("Total =", total)

average = total / count

print('The average of your numbers is', average)
print('The total of your numbers is', total)

#Enhacement - Replace user input with random number generator
import random

print('\nEnhanced Program')
totalE = 0
countE = 0

while totalE <= 45:
    numE = random.randint(1,45)
    totalE += numE
    countE += 1
    print("Number =", numE)
    print("Total =", totalE)

averageE = totalE / countE

print('The average of the numbers is', averageE)
print('The total of the numbers is', totalE)