#1 list(): chuyển đổi kiểu dữ liệu của một biến sang dạng list

#2 len(): tra ve so luong phan tu

#3 max(): tra ve phan lon nhat, cuoi, dai nhat

#4 min():

#5 append(): noi them vao cuoi

#6 extend(): ke thua

#7 count(): dem so luong xuat hien

#8 index(): trả về index xuất hiện đầu tiên của phần tử mà bạn muốn tìm 
#và nếu như không tìm thấy thì nó sẽ gọi exception.

#9 insert(): thêm phần tử vào vị trí index của list, 
#và các phần tử sau index đó sẽ được đẩy về phía sau.

#10 reverse(): dao nguoc list

#11 remove(): xoa phan tu

#12 pop(): xóa bỏ phần tử trong list dựa trên index của nó, default = -1

#13 sort(): sap xep
#mylist.sort(reverse, key) : default reverse = false (tu be->lon), key = call back
list = ['A', 'C', 'B', 'E', 'D']

list.sort()
print(list)
# Kết quả: ['A', 'B', 'C', 'D', 'E']

list.sort(reverse=True)
print(list)
# Kết quả: ['E', 'D', 'C', 'B', 'A']


def custom_sort(elem):
    return elem[1]
list = [(1, 2), (5, 7), (7, 100), (4, 4)]
list.sort(reverse=True, key=custom_sort)
print(list)
# Kết quả: [(1, 2), (4, 4), (5, 7), (7, 100)]

#14 clear(): delete all