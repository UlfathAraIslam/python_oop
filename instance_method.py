class Student:
    def __init__(self,name,Id):
        self.name = name
        self.id = Id
    def details(self): # instance method
        print("Name:",self.name,"ID:",self.id)
s1 = Student("Bob",11)
s2 = Student("rob",12)
s1.id = 133
s1.details()
s2.details()