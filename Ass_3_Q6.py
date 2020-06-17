#Files

READ = 'r'
APPEND = 'a'
fileName = 'MyPythonNotes.txt'

file = open(fileName, mode = READ)
print(file.read())
file.close

file = open(fileName, mode = APPEND)
file.write(input('Please enter an interesting 11th fact: '))
print('Thank you, we have 11 facts')
print('\nThe current content of the file is;')
file.close

file = open(fileName, mode = READ)
print(file.read())
file.close