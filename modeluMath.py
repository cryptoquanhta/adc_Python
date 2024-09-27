#1 abs(): trả về giá trị tuyệt đối của một số.
number = -5
print(abs(number))
#---ko can import math

import math
#2 fabs(): khác với hàm abs() ở trên là hàm này sẽ chỉ chấp nhận chuyển đổi được kiểu số nguyên (integer) 
#và số thực (float) trong khi hàm abs() chuyển đổi được cả complex number.
#math.fabs(number)

#3 ceil(): lam tron len 1 dvi
number2 = -19.6
print(math.ceil(number2))
# Kết quả: -19

#4 exp(): trả về kết quả e^x

#5 floor(): lam tron xuong

#6 log(): kết quả logarithm x

#7 log10():

#8 max(): trả về số lớn nhất trong các số được truyền vào.
#---ko can import math
x, y, z = 5, 1, 3
print(max(x, y, z))

#9 min(): 

#10 modf(): chuyển đổi một số về một tuple. 
#Tuple này chứa phần thập phân và phần nguyên của số đó, 
#lưu ý tất cả các giá trị trong tuple này đều ở dạng float.
x = 5.278
print(math.modf(x))
# Kết quả: (0.2779999999999996, 5.0) 

#11 pow(): trả về kết quả của phép xy, với x là tham số thứ nhất, y là tham số thứ 2.
x, y = 5, 2
print(math.pow(x, y))
# Kết quả: 25.0

#12 round(): lam tron den gia tri gan nhat
#---ko can import math
#math.round(number, count = 0)

#13 sqrt(): về căn bậc 2 của một số, với điều kiện số đó phải lớn hơn 0.
x = 9
print(math.sqrt(x))
# Kết quả: 3.0