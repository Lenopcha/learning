def repack_boxes(original_boxes, bars_per_new_box):
    # Total number of bars
    total_bars = sum(original_boxes)

    # Number of new boxes
    new_boxes = total_bars // bars_per_new_box

    # Remaining bars
    remaining_bars = total_bars % bars_per_new_box

    # Leftover boxes
    leftover_boxes = []
    if remaining_bars > 0:
        leftover_boxes.append(remaining_bars)

    # Print the result
    leftover_boxes_count = len(leftover_boxes)
    print(
        f"new boxes: {new_boxes}, left: {leftover_boxes_count} box{'es' if leftover_boxes_count != 1 else ''} with {remaining_bars} bar{'s' if remaining_bars != 1 else ''}")

    return new_boxes, leftover_boxes


# Example usage:
original_boxes = [2, 3, 1, 5]
bars_per_new_box = 5
repack_boxes(original_boxes, bars_per_new_box)
