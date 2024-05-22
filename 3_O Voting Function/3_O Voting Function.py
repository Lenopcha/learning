def major(x, y, z):
    # Count the occurrences of True and False
    true_count = sum([x, y, z])
    false_count = 3 - true_count

    # Return the value that occurs most frequently
    if true_count > false_count:
        return True
    else:
        return False

# Example usage:
print(major(False, True, False))  # Output: False
print(major(True, True, False))   # Output: True
print(major(False, False, False)) # Output: False
print(major(True, True, True))    # Output: True
