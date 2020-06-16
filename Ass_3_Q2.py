#Functions

def my_greatest(a,b,c):
    average = (a+b+c) / 3
    print('The average of the three numbers is', average)
    return a,b,c

number1 = int(input('Please enter the first number: '))
number2 = int(input('Please enter the second number: '))
number3 = int(input('Please enter the third number: '))

my_greatest(number1,number2,number3)