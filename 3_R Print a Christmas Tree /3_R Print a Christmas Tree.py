def triangle(n, extra_spaces):
    for i in range(n):
        num_stars = 1 + 2 * i
        num_spaces = n - i - 1
        print(' ' * (num_spaces + extra_spaces) + '*' * num_stars)

def fir(a, b):
    for height in range(a, b + 1):
        triangle(height, b - height)

# Example usage
fir(2, 4)
