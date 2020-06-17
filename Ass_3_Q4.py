#Class Instances

class Cats():
    def __init__(self):
        self.catName = ''
        self.catAge = 0
        
    def populate(self, catName, catAge):
        self.catName = catName
        self.catAge = catAge
        
    def display(self):
        print('Cat name is:', self.catName.capitalize())
        print('Cat age is:', self.catAge)

instance1 = Cats()
instance2 = Cats()
instance3 = Cats()
instance4 = Cats()
instance5 = Cats()

instance1.populate(input("Enter cat name: "),int(input('Enter cat age: ')))
instance2.populate(input("Enter cat name: "),int(input('Enter cat age: ')))
instance3.populate(input("Enter cat name: "),int(input('Enter cat age: ')))
instance4.populate(input("Enter cat name: "),int(input('Enter cat age: ')))
instance5.populate(input("Enter cat name: "),int(input('Enter cat age: ')))

instance1.display()
instance2.display()
instance3.display()
instance4.display()
instance5.display()
