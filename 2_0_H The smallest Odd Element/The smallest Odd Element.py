print("Just give me some numbers, separated by spaces: ")
numbers = [int(x) for x in input().split()]
minimum = max(numbers)
found = False


for num in numbers:
    if num % 2 != 0 and num < minimum:
        minimum = num
        found = True

if found == True:
    print(f"The minimum odd number is: {minimum}")
else:
    print("0")
