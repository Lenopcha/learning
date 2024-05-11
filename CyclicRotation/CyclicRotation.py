def solution(A, K):
    # Calculate the effective number of rotations
    K %= len(A)

    # If no rotation is needed, return the array as is
    if K == 0:
        return A

    # Create a new array to store the rotated elements
    rotated_array = [None for _ in range(len(A))]

    # Copy the last K elements to the beginning of the new array
    for i in range(K):
        rotated_array[i] = A[len(A) - K + i]

    # Copy the first N - K elements to the remaining positions
    for i in range(len(A) - K):
        rotated_array[i + K] = A[i]

    return rotated_array


# Test cases
print(solution([3, 8, 9, 7, 6], 3))  # Output: [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))  # Output: [0, 0, 0]
print(solution([1, 2, 3, 4], 4))  # Output: [1, 2, 3, 4]


