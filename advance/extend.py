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

#Ghi đè:
#Trong trường hợp cả hai class cha và con tồn tại các thuộc tính và phương thức có cũng tên, 
#thì trong Python sẽ nó sẽ ưu tiên thực thi và gọi các phương thức và thuộc tính khai báo trong class được khởi tạo.

#Super: Trong trường hợp ở class con mà bạn muốn sử dụng đến các thành phần trong class cha
# thì bạn phải sử dụng hàm super theo cú pháp sau:
# Đối với thuộc tính.
#super().variableName
# Đối với phương thức.
#super().methodName()

#Đa kế thừa
class First:
    def getFirst(self):
        print("Class Fist")
        
class Second:
    def getSecond(self):
        print("Class Second")

class Third(First, Second):
    def getThird(self):
        print("Class Third")

third = Third()
third.getFirst()
third.getSecond()
third.getThird()

# Kết Quả:
# Class Fist
# Class Second
# Class Third