def rotate_array(A, K):
    if len(A) == 0:
        return A

    K = K % len(A)
    return A[-K:] + A[:-K]

def validate_array_input(user_input):
    elements = user_input.split()
    if all(-1000 <= int(num) <= 1000 for num in elements):
        return True
    return False

def validate_rotation_input(user_input):
    if user_input.isdigit() and 0 <= int(user_input) <= 100:
        return True
    return False

def validate_try_again_input(user_input):
    if user_input.lower() in ['y', 'n']:
        return True
    return False

def get_input(prompt, validator):
    while True:
        user_input = input(prompt).strip()
        if validator(user_input):
            return user_input
        print("Invalid input. Please try again.")

def main():
    while True:
        A = list(map(int, get_input("Enter the elements of the array (-1000 to 1000, separated by space): ",
                                    validate_array_input).split()))

        print("Original array:", A)

        K = int(get_input("Enter the number of rotations (0 to 100): ",
                          validate_rotation_input))

        # Rotate the array
        rotated_array = rotate_array(A, K)
        print("Rotated array:", rotated_array)

        # Ask the user if they want to try again
        try_again = get_input("Do you want to try again? (y/n): ", validate_try_again_input)
        if try_again == 'n':
            print("Goodbye!")
            break

main()
