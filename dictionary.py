#Kiểu dữ liệu dictionary trong Python là một kiểu dữ liệu 
# lưu trữ các giá trị chứa key và value , 
# nhìn một cách tổng quát thì nó giống với Json
person = {
    'name': 'Vũ Thanh Tài',
    'age': 22,
    'male': True,
    'status': 'single'        
    }
person['status'] = 'married'
print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True, 
# 'status': 'married'}

#Delete
#del person['status']
#dictName.clear();
#{}

#Dictionary Long
person2 = {
    'name': 'Vũ Thanh Tài',
    'option': {
                'age': 22,
                'male': True,
                'status': 'alone'
            }        
    }

print(person2['option']['age'])
# 22