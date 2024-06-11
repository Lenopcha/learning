def repack_boxes(original_boxes, bars_per_new_box):
    # Total number of bars
    total_bars = sum(original_boxes)

    # Number of new boxes
    new_boxes = total_bars // bars_per_new_box

    # Remaining bars
    remaining_bars = total_bars % bars_per_new_box

    # Calculate leftover boxes
    leftover_boxes = []
    current_bars = remaining_bars

    if remaining_bars > 0:
        for box in original_boxes:
            if box <= current_bars:
                leftover_boxes.append(box)
                current_bars -= box
            else:
                if current_bars > 0:
                    leftover_boxes.append(current_bars)
                break

    # Print the result
    leftover_boxes_count = len(leftover_boxes)
    remaining_bars_list = ', '.join(map(str, leftover_boxes))
    print(
        f"new boxes: {new_boxes}, left: {leftover_boxes_count} box{'es' if leftover_boxes_count != 1 else ''} with {remaining_bars_list} bar{'s' if remaining_bars != 1 else ''}")

    return new_boxes, leftover_boxes


# Example usage:
original_boxes = [2, 3, 1, 5]
bars_per_new_box = 5
repack_boxes(original_boxes, bars_per_new_box)
