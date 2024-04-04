my_list = list(map(int, input("Введіть список цілих чисел, розділених пробілами"
                              "(обов'язково додайте принаймні одне позитивне): ").split()))
index = 0

# go through list to find a positive element
while my_list[index] <= 0:
    index += 1
print("Index of first positive element:", index)
