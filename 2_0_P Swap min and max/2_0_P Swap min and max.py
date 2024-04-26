numbers = list(map(int, input("Give me some numbers: ").split()))
print(numbers)
max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
print(numbers)
