#khai bao class

class Person:
    name = 'Kevin'
    age = 22
    male = True

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

person = Person()

print(person.name)
person.setName('Kevin Nguyen')
print(person.getName())