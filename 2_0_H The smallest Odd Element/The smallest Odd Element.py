my_input = input("Just give me some numbers, separated by spaces: ")

minimum = 9999
number = ""  # Змінна для роботи з поточним для циклу

for i in my_input:
    if i != " ": #не пробіл (щоб визачити коли кінець циклу)
        number += i
    else:
        if number:
            num = int(number)
            if num % 2 != 0 and num < minimum:
                minimum = num
            number = ""  #роблю змінну пустою

if number:
    num = int(number)
    if num % 2 != 0 and num < minimum:
        minimum = num

if minimum != 9999:
    print(f"The minimum odd number is: {minimum}")
else:
    print("0")


