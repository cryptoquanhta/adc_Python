#Tuple trong Python là một kiểu dữ liệu dùng để lưu trữ các đối 
# tượng không thay đổi về sau (giống như hằng số).
day = ('monday', 'tuesday', 'wednesday' , 'thursday', 
       'friday', 'saturday' , 'sunday')

#Xoa tuple
# del day

#Them moi
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday')
day3 = day1 + day2
# ('monday', 'tuesday', 'wednesday', 'thursday', 
# 'friday', 'saturday', 'sunday')

#Tuple long
day4 = ('monday', 'tuesday', 'wednesday')
day5 = ('thursday', 'friday', 'saturday' , 'sunday', day4)
#print(day5)
# ('thursday', 'friday', 'saturday', 
# 'sunday', ('monday', 'tuesday', 'wednesday'))
print(day5[4][0]) # monday