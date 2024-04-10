
numbers = list(map(int, input("Введіть список цілих чисел, розділених пробілами: ").split()))
index = 0

while index < len(numbers) and numbers[index] <= 0:
    index += 1

if index == len(numbers):
    print("-1")
else:
    print("Індекс першого позитивного елемента:", index)
    print("Значення першого позитивного елемента:", numbers[index])
