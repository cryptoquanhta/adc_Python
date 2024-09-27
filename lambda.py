#Lambda là một anonymous function (hàm ẩn danh) nó có thể khai báo, 
#định nghĩa ở bất kỳ đâu và không có khả năng tái sử dụng.

#Lambda chỉ tồn tại trong phạm vi của biến mà nó được định nghĩa, 
#vì vậy nếu như biến đó vượt ra ngoài phạm vi thì hàm này cũng không còn tác dụng nữa.

#Lambda thường được dùng để gán vào biến, hay được gán vào hàm, class như một tham số.

add = lambda a, b: a + b

# call lambda
add(3, 4) # 7