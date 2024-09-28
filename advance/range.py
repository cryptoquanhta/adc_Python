#1 Public
#2 Protected = Public
#phạm vi sử dụng ở trong class khởi tạo nó và class kế thừa từ class đó (class con)
# mà chúng ta sẽ không thể gọi được khi đứng từ bên ngoài class.
#Tên của thành phần phải được bắt đầu bằng 1 ký tự _

#3 Private
#Tên cả thành phần phải được bắt đầu bằng 2 ký tự __.
class Foo:
    # Khai báo thuộc tính ở chuẩn private
    __name = "Foo"
    # Khai báo phương thức ở chuẩn private
    def __getName(self):
        # gọi thành phần trong class
        print(self.__name)
    # khai báo một phương thức ở dạng public để gọi thành phần private
    def get(self):
        self.__getName()

# gọi thành phần ngoài class
print(Foo().__name) # 'Foo' object has no attribute '__name'
Foo().__getName() # 'Foo' object has no attribute '__getName'
Foo().get() # Foo

class Bar(Foo):
    def getNameinFoo(self):
        self.__getName()

#test
Bar().getNameinFoo() # 'Bar' object has no attribute '_Bar__getName'