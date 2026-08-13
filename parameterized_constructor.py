class Student:
    def __init__(self,name,Id):
        self.name = name        #instance variable
        self.id = Id            #instance variable

s1 = Student("Bob",11)
s2 = Student("Carol",22)
s1.id = 33
print(s1.name)
print(s1.id)