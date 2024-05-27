def triangle(n):
    for i in range(n):
        num_stars = 1 + 2 * i
        num_spaces = n - i - 1
        print(' ' * num_spaces + '*' * num_stars)

while True:
    try:
        n = int(input("Enter a positive integer for the size of the triangle: "))
        if n > 0:
            triangle(n)
            break
        else:
            print("The number must be positive.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
