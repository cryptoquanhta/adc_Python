#Abstract là một class, và class này chứa một hoặc nhiều phương thức trừu tượng.
#Abstract class không thể khởi tạo trực tiếp được.
#Một class kế thừa từ abstract class thì bắt buộc phải khai báo lại
# các các phương thức trừu tượng có trong abstract mà nó kết thừa.
from abc import ABC, abstractmethod

class PersonAbstact(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)
    @abstractmethod
    def getFull(self):
        pass

class Person(PersonAbstact):
    name = 'Kevin nguyen'
    age = 22
    def getFull(self):
        self.getName()
        self.getAge()

Person().getFull();
# Kết Quả:
# Kevin nguyen
# 22