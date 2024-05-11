def rotate_array(A, K):
    if not A:
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]


def main():
    # Ask the user for the elements of the array
    while True:
        try:
            A = list(map(int, input("Enter the elements of the array (-1000 to 1000, separated by space): ").split()))
            if not all(-1000 <= num <= 1000 for num in A):
                raise ValueError
            break
        except ValueError:
            print("Please enter valid integers between -1000 and 1000, separated by space.")

    print("Original array:", A)

    # Ask the user for the number of rotations
    while True:
        try:
            K = int(input("Enter the number of rotations (0 to 100): "))
            if not 0 <= K <= 100:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid integer between 0 and 100 for the number of rotations.")

    # Rotate the array
    rotated_array = rotate_array(A, K)
    print("Rotated array:", rotated_array)

    # Ask the user if they want to try again
    while True:
        try_again = input("Do you want to try again? (y/n): ").strip().lower()
        if try_again == 'y':
            main()
            break
        elif try_again == 'n':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


main()
