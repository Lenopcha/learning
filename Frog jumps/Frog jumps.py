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
    print("Once upon a time, there was a little frog on a journey.")
    print(f"The frog started at position {current_position}.")

    for i in range(1, jumps + 1):
        # Calculate the new position after the jump
        new_position = current_position + D

        # Simulate an encounter or activity at the current position
        if i == 1:
            print(f"The frog met a friendly squirrel at position {new_position}. They shared a cup of tea.")
        elif i == jumps:
            print(f"The frog reached a cozy pond at position {new_position}. It took a nap before realizing it has reached its destination!")
            break
        else:
            print(f"The frog hopped along and reached position {new_position}. It journaled its journey before continuing.")

        # Update the current position for the next jump
        current_position = new_position

    print("The frog finally reached its destination!")

    return jumps

# Example usage of the function
X = 10
Y = 85
D = 30
print(f"Minimal number of jumps: {solution(X, Y, D)}")
