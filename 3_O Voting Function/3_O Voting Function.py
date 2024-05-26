def major(*args):
    # Count the occurrences of True
    true_count = sum(args)

    # Calculate the half length
    half_length = len(args) / 2

    # Determine and return the majority value
    if true_count > half_length:
        return True

    return False


# Example usage:
print(major(False, True, False))  # Output: False
print(major(True, True, False))  # Output: True
print(major(False, False, False))  # Output: False
print(major(True, True, True))  # Output: True
print(major(True, False, True, False, True))  # Output: True
print(major(True, False, False, False))  # Output: False

