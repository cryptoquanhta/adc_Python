def sum(a,b):
    return a / b

try :
    print(sum(6, 0))
except ZeroDivisionError:
    print('Co loi xay ra')
finally:
    print('finally dc call')