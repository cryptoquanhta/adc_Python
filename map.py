def mutiply(x):
    return x * x
result = map(mutiply, [1, 2, 3, 4])
print(list(result)) # [1, 4, 9, 16]

result = map(lambda x: x * x, [1, 2, 3, 4])
print(list(result))  # [1, 4, 9, 16]

#2 var
result = map(lambda x, y: x + " " + y, ['red', 'blue'], ['green', 'black'])
print(list(result))  # ['red green', 'blue black']

def map2(x, y):
    return x + " " + y
result = map(map2, ['red', 'blue'], ['green', 'black'])
print(list(result))  # ['red green', 'blue black']
