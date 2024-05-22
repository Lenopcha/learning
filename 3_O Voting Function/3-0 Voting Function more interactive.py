def major(x, y, z):
    # Create a list of the values
    values = [x, y, z]

    # Count the number of True values
    true_count = values.count(True)

    # Print the number of True values found
    print(f"Number of True values: {true_count}")

    # print the result
    if true_count >= 2:
        result = True
        print(f"The majority of the values are True. Returning: {result}")
    else:
        result = False
        print(f"The majority of the values are False. Returning: {result}")

    return result


def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['true', 'false']:
            return user_input == 'true'
        print("Invalid input. Please enter 'true' or 'false'.")


def main():
    print("Welcome to the Majority Voting Program!")
    print("Please enter three boolean values (true or false).")

    x = get_boolean_input("Enter the first value (true/false): ")
    y = get_boolean_input("Enter the second value (true/false): ")
    z = get_boolean_input("Enter the third value (true/false): ")

    print(f"You entered: x = {x}, y = {y}, z = {z}")

    result = major(x, y, z)

    print(f"The result of the majority voting is: {result}")

    print("Thank you for using the program!")


main()
