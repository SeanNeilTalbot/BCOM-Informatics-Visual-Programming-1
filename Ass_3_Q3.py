#Classes

class Cats():
    def __init__(self, catName, catAge):
        self.catName = ''
        self.catAge = 0
        
    def populate(self):
        self.catName = catName
        self.catAge = catAge
        
    def display(self):
        print('Cat name is:', self.catName.capitalize())
        print('Cat age is:', self.catAge)

catName = input("Enter cat name: ")
catAge = int(input('Enter cat age: '))

run = Cats(catName,catAge)
run.populate()
run.display()
