#1
result_1 = []
for i in range(100, 0, -1):
    result_1.append(i ** 2)
print(result_1)

#2
result_2 = list(map(lambda x: x ** 2, range(100, 0, -1)))
print(result_2)

#3
result_3 = [i ** 2 for i in range(100, 0, -1)]
print(result_3)
