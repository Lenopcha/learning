numbers = list(map(int, input("Enter a list of numbers separated by spaces:").split()))
index = 0

while index < len(numbers) - 1 and numbers[index] * numbers[index + 1] <= 0:
    index += 1

if index < len(numbers) - 1:
    print("Found a pair of numbers of the same sign:")
    print(numbers[index], numbers[index + 1])
else:
    print("No pair of numbers of the same character found.")
