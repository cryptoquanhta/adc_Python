#Hàm này cũng có tác dụng duyệt qua các phần tử trong list, dict,... 
#nhưng khác với map là hàm này sẽ chỉ trả về những giá trị mà điều kiện trong function chấp nhận (có nghĩa là True).

result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])
#print(result) <filter object at 0x0000017942BF9660>
print(list(result))  # [1, 3, 5, 7, 9]