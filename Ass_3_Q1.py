#Functions

def my_greet(name):
    print('Good day,', name.capitalize())
    return name

name = input('Please enter your name: ')

my_greet(name)