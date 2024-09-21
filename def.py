def say():
    print("Welcome to Python")
say()
def sum(a, b):
    print("sum = " + str(a+b))
sum(1,2)

#def co return
def plus(a, b):
    return a+ b
c = plus(2, 3)
print("Tong cua 2 va 3 = " + str(c))

#pham vi cua bien trong ham: chi dung trong ham do, nhung neu la List thi se thay doi dc

d = [5, 10, 15]
def change(d):
    d[0] = 1
    print(d)
change(d)
# KQ: [1, 10, 15]
print(d)

# Global variable: global tenbien

# Truyen vo so tham so:
def get_sum(*num):
    tmp = 0
    # duyet cac tham so
    for i in num:
        tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)

print(result)
# KQ: 15