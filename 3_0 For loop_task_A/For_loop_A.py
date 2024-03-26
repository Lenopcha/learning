
my_list = [1, 5]
#1

my_new_list = []
for i in range(my_list[0], my_list[1]+1):
    my_new_list.append(i)
print(my_new_list)

#2
my_new_list_2 = list(map(lambda x: x, range(my_list[0], my_list[1] + 1)))
print(my_new_list_2)

#3
my_new_list_3 = [x for x in range(my_list[0], my_list[1] + 1)]
print(my_new_list_3)
