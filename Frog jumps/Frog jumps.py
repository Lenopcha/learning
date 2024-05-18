def solution(X, Y, D):
    # Calculate the distance to be covered
    distance = Y - X

    # Determine the number of jumps needed to cover this distance
    jumps = distance // D

    # If there's a remainder after division, it means an extra jump is needed
    # to cover the remaining distance
    if distance % D != 0:
        jumps += 1

    # Initialize the current position of the frog
    current_position = X

    # Print the story and each step in the calculation process
    print("Once upon a time, there was a little frog who met a friend on its journey.")
    print(f"The frog started its journey from position {X} and wanted to reach position {Y}.")
    print(f"The frog could jump {D} units per jump.")
    print("The journey began...")

    for i in range(1, jumps + 1):
        # Calculate the new position after the jump
        new_position = current_position + D

        # Print the progress and current position after each jump
        print(f"After the {i}{'st' if i == 1 else 'nd' if i == 2 else 'th'} jump,")
        print(f"the frog landed at position {new_position}.")

        # Update the current position for the next jump
        current_position = new_position

    print("The frog finally reached its destination!")

    return jumps

# Example usage of the function
X = 10
Y = 85
D = 30
print(f"Minimal number of jumps: {solution(X, Y, D)}")
