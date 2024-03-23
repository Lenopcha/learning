my_input = input("Just give me some numbers, separated by spaces: ")
numbers = [int(x) for x in my_input.split()]
minimum = int(max(my_input))

for num in numbers:
    if num % 2 != 0 and num < minimum:
        minimum = num

if minimum != int(max(my_input)):  # Якщо мінімум оновлено (знайдено непарне число)
    print(f"The minimum odd number is: {minimum}")
else:
    print("0")
