print ('Hello world!', end = '- Python')
#Kieu du lieu
name, age, male = "Kevin", 26, True
tuple = ('Kevin tuple', 26, True)
dictionary = {"name": "Kevin dictionary", "age":22, "male":True }
print(dictionary)

#Chuoi trong Python
print('Website \'Kevin di code\' ')
#\n ngắt xuống dòng và bắt đầu dòng mời.
#\t đẩy nội dung phía sau nó cách 1 tab.
#\a chuông cảnh báo.
#\b xóa bỏ khoảng trắng phía trước nó.

#Binding du lieu
guy = "Ban"
doamin = "Kevin di code"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)
# Chao mung Ban den voi website Kevin di code

#Truy cap tung gia tri cua chuoi
print(name[0:3])