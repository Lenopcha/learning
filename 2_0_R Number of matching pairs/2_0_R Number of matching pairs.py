numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

pair_count = 0

# Nested loop to compare elements
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pair_count += 1

print("The number of pairs of elements that are equal to each other:", pair_count)
