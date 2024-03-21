#my_list = [1, 5, 3, 4, 2]
my_list = input("Just give me some numbers: ")
copy_list = my_list[:]

for i in range(len(copy_list)):
    if i > 0 and copy_list[1] > copy_list[i - 1]:
        print(copy_list[i])
