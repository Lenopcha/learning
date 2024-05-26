def major(*args):
    # Convert arguments to list
    values = list(args)

    # Count the number of True values
    true_count = values.count(True)

    # Print the number of True values found
    print(f"Number of True values: {true_count}")

    # Determine and print the result
    result = true_count > len(values) // 2
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

    values = []
    for i in range(1, 4):
        value = get_boolean_input(f"Enter value {i} (true/false): ")
        values.append(value)
        print(f"Value {i} is {value}.")
        if value:
            print(f"Value {i} is True, adding to the True count.")
        else:
            print(f"Value {i} is False, not adding to the True count.")

    print(f"You entered: {values}")

    result = major(*values)

    print(f"The result of the majority voting is: {result}")

    print("Thank you for participating in the program!")

# Run the main function
main()
