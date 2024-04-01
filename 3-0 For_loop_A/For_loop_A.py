
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

# 1.
my_new_list = []
for i in range(start, end + 1):
    my_new_list.append(i)
print(my_new_list)

# 2.
my_new_list_2 = [x for x in range(start, end + 1)]
print(my_new_list_2)

# 3.
my_new_list_3 = list(map(lambda x: x, range(start, end + 1)))
print(my_new_list_3)
