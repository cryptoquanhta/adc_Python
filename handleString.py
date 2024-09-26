string = 'Kevin Nguyen'
#1 Capitallize()

#2 Center(): tra ve chuoi o giua

#3 count()
print(string.count('i'))

#4 encode()

#5 decode()

#6 endswith(): co ket thuc vs ky tu ko

#7 expandtabs(): thay the \t bang 1 khoang trang len = 8

#8 find(): tra ve vi tri bat dau

#9 index(): giong find(), neu ko thay tra ve exception

#10 isalnum(): tra ve true neu chi chua number and string

#11 isalpha(): tra ve true neu chi chua string

#12 isdigit(): = true neu chứa duy nhất các chữ số

#13 islower(): = true neu in thuong

#14 isupper(): = true neu in hoa

#15 isnumeric(): = true neu chỉ chứa duy nhất các ký tự số

#16 isspace(): = true neu chi chua khoang trang

#17 istitle(): = true neu string la title(cac chu cai dau tien viet hoa)

#18 join()
string_one = ' '
string_two = 'TAI'
print(string_one.join(string_two))
# Kết quả: T A I
string_one1 = '-'
string_two1 = ['T','D','C',]
print(string_one1.join(string_two1))
# Kết quả: T-D-C

#19 len(): do dai cua chuoi

#20 ljust(): tra ve mot chuoi voi do dai xac dinh

#21 rjust(): sẽ bù về phía bên trái của chuỗi

#22 lower(): chuyen ve in thuong

#23 upper(): chuyen ve in hoa

#24 lstrip(): loại bỏ đi các ký tự char ở phía đầu của chuỗi

#25 rstrip(): cuoi chuoi

#26 strip(): = lstrip + rstrip

#27 rfind(): tra ve ky tu cuoi ben right

#28 rindex(): tra ve ky tu dau tien ben right

#29 replace(): string.replace(old, new, max)

#30 max() min(): max(string) tra ve ky tu cuoi cung trong bang chu cai

#32 title(): convert chuoi sang dang title

#33 swapcase(): chuyển đổi chuỗi sang dạng nghịch đảo của nó (nghịch đảo ở đây là hoa - thường).

#34 zfill(): thêm được các ký tự zero (số 0) và trước chuỗi thôi

#35 isdecimal(): return = true neu string chi chua cac so thap phan

#36 split(): tach string thanh mang boi ky tu (char)
print(string.split('a'))

#37 splitlines(): tach chuoi boi ky tu \n

#38 startswith(): ktra xem chuoi co dc bat dau bang ky tu ko
print(string.startswith('k'))

#39 maketrans()

#40 translate()
