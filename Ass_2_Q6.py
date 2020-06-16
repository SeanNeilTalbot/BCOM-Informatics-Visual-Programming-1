#Tuples and Sets

subjectTuple = ('Math','Science','Business Studies','Geography','Applied Math','Information Technology','English','Math Paper 3')

print('The first element is', subjectTuple[0])
print('The last element is', subjectTuple[-1])
print('The length of the tuple is', len(subjectTuple))

subject = input('Please input the matric subject: ')

if subject.capitalize() in subjectTuple:
    print('That subject is in the list')

else:
    print('That subject is not in the list')