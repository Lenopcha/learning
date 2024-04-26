
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Cycle for exchanging adjacent elements
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]


print("Result of swapping neighboring elements:", *numbers)
