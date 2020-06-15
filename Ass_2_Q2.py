#Use of for loop, integers and user input

num1 = int(input("Please enter the first number of 5: "))
num2 = int(input("Please enter the second number of 5: "))
num3 = int(input("Please enter the third number of 5: "))
num4 = int(input("Please enter the fourth number of 5: "))
num5 = int(input("Please enter the fifth number of 5: "))

print("Your numbers are:")
for n in (num1,num2,num3,num4,num5):
    print(n)

sum = num1 + num2 + num3 + num4 + num5
print("The sum of your numbers is: ",sum)

average = sum / 5
print("The average of your numbers is: ", average)