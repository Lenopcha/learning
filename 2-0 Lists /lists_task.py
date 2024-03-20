my_list = input("Just give me some numbers: ")
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(my_list[0::2])
for i in range(0, len(my_list), 2):
    print(my_list[i])
