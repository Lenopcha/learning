#my_list = [1, 2, 3, 2, 1]
my_list = input("Give me some numbers: ")
maximum = max(my_list)
index = my_list.index(maximum)

print(f"Number {maximum} is largest. Index: {index}")