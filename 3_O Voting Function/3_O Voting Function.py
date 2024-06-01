def major(*args):
    # Count the occurrences of True and False
    true_count = args.count(True)
    false_count = args.count(False)

    # Determine and return the majority value
    if true_count > false_count:
        return True
    return False


# Example usage:
print(major(False, True, False))  # Output: False
print(major(True, True, False))  # Output: True
print(major(False, False, False))  # Output: False
print(major(True, True, True))  # Output: True
print(major(True, False, True, False, True))  # Output: True
print(major(True, False, False, False))  # Output: False
