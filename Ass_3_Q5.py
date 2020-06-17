#Files

import sys

APPEND = 'a'
READ = 'r'
fileName = 'MyPythonNotes.txt'

file = open(fileName, mode = APPEND)

for i in range(10):
    print('Fact Number:', i+1)
    fact = input('Enter an interesting fact about Python: ')
    file.write(fact)
    file.write('\n')

    if i == 9:
        print('\nThank you, we now have 10 facts\n')
file.close

file = open(fileName, mode = READ)
print("The current content of the file is:")
print(file.read())
file.close