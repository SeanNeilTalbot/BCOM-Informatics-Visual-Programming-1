#Using strings, user input, character characteristics

userInput = input("Please enter a sentence.")

print(userInput)
print('The sentence is', len(userInput), 'characters long.')
print('The sentence max is:', max(userInput))
print('The sentence min is:', min(userInput))
print('The sentence titlized is:', userInput.title())
print('The sentence capitalized is:', userInput.capitalize())