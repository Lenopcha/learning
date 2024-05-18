def solution(X, A):
    covered_positions = set()  # Set to track covered positions
    print("After a series of jumps, our little frog reaches the bank of a river.\n"
          "The frog now faces a new challenge: crossing the river with the help of falling leaves.\n"
          "The frog sits down and starts counting the leaves falling into the river, hoping to see all positions covered.\n")

    for i in range(len(A)):
        # Frog encounters a leaf
        leaf_position = A[i]
        print(f"At second {i}, a leaf falls on position {leaf_position}.")

        # Add the leaf position to covered positions
        covered_positions.add(leaf_position)

        # Check if all positions are covered
        if len(covered_positions) == X:
            print(f"By second {i}, all positions from 1 to {X} are covered!\n"
                  "The frog checks its travel map and sees it can now jump to the other side.\n"
                  "With a big leap, the frog successfully crosses the river and continues its adventure.\n")
            return i

    # If not all positions were covered
    print("Unfortunately, the frog was never able to cross the river.\n")
    return -1

# Test the function with an example
X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print("Earliest time when the frog can jump to the other side:", solution(X, A))
print()

# Here we can add a loop to interactively test the function with different inputs
def main():
    while True:
        try:
            # Ask for the position X
            X = int(input("Enter the position X (the other side of the river): "))
            print()

            # Ask for the array A
            A_input = input("Enter the positions of falling leaves (space-separated): ")
            A = list(map(int, A_input.split()))
            print()

            # Call the function with the input data
            result = solution(X, A)
            print(f"Earliest time when the frog can jump to the other side: {result}\n")

            # Ask if the user wants to try again
            try_again = input("Do you want to try again? (y/n): ").strip().lower()
            print()
            if try_again != 'y':
                break
        except ValueError:
            print("Invalid input. Please try again.\n")

main()
