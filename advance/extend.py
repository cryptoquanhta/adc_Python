class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def getName(self):
        print("Name: %s" %(self.name))
    def getAge(self):
        print("Age: %d" %(self.age))
    def getSex(self):
        print("Sex: %s" %(self.sex))

class Male(Person):
    sex = "Male"

male = Male("Kevin Nguyen", 22)
male.getName()
male.getAge()
male.getSex()

# Ket qua:
# Name: Kevin Nguyen
# Age: 22
# Sex: Male