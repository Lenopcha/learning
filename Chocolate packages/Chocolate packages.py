def repack_boxes(original_boxes, bars_per_new_box):
    # Calculate the total number of bars
    total_bars = sum(original_boxes)

    # Calculate the number of new boxes
    new_boxes = total_bars // bars_per_new_box

    # Calculate the remaining bars after repacking
    remaining_bars = total_bars % bars_per_new_box

    # Determine the number of leftover boxes
    leftover_boxes = 1 if remaining_bars != 0 else 0

    # Print the result
    print(
        f"new boxes: {new_boxes}, left: {leftover_boxes} box with {remaining_bars} bar{'s' if remaining_bars != 1 else ''}")

    return new_boxes, (leftover_boxes, remaining_bars)


# Example usage::
original_boxes = [2, 3, 1, 5]
bars_per_new_box = 5
repack_boxes(original_boxes, bars_per_new_box)
