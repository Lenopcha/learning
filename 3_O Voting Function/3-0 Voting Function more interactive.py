def major(*args):
    # Convert arguments to list
    values = list(args)

    # Count the occurrences of True and False
    true_count = values.count(True)
    false_count = values.count(False)

    # Print the number of True and False values found
    print(f"Number of True values: {true_count}")
    print(f"Number of False values: {false_count}")

    # Determine and print the result
    result = true_count > false_count
    print(f"The majority of the values are {'True' if result else 'False'}. Returning: {result}")
    return result


def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['true', 'false']:
            return user_input == 'true'
        print("Invalid input. Please enter 'true' or 'false'.")


def main():
    print("Welcome to the Interactive Majority Voting Program!")
    print("In this program, you will enter three boolean values (true or false).")

    bool1 = get_boolean_input("Enter the first boolean value (true/false): ")
    bool2 = get_boolean_input("Enter the second boolean value (true/false): ")
    bool3 = get_boolean_input("Enter the third boolean value (true/false): ")

    # Call the major function with the user inputs
    result = major(bool1, bool2, bool3)
    print(f"\nThe result of the majority voting is: {result}")


# Start the interactive program
main()