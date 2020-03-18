def merge_sort(unsorted, threshold, reverse):
    """
    if length of unsorted is less than threshold then 
    call insertion sort and return unsorted. Else split until below threshold and merge.
    """
    i = 0
    k = len(unsorted) - 1

    if k <= threshold:
        print("pre insertion:", unsorted)
        unsorted = insertion_sort(unsorted[i:k+1], reverse)
        print("post insertion:", unsorted)
        return unsorted

    else:

        j = (i + k) // 2  # Find the midpoint in the partition
        unsorted_left = merge_sort(unsorted[:j+1], threshold, reverse)
        print("Left val:", unsorted_left)
        unsorted_right = merge_sort(unsorted[j+1:], threshold, reverse)
        print("Right val:", unsorted_right)
        unsorted = merge(unsorted_left, unsorted_right, reverse)
        return unsorted

def merge(first, second, reverse):

    """
    :param first: first list to merge
    :param second: second list to merge
    :param reverse: boolean for reverse
    :return: merged list
    """

    j = len(first)-1
    k = len(second)-1
    merged_size = len(first) + len(second)  # Size of merged partition
    print(merged_size)
    merged_numbers = [0] * merged_size
    # for merged numbers
    merge_pos_true = merged_size - 1
    merge_pos_false = 0  # Position to insert merged number
    left_pos = 0  # Initialize left partition position
    right_pos = 0   # Initialize right partition position

    if reverse is False:

        # Add smallest element from left or right partition to merged numbers
        while left_pos <= j and right_pos <= k:
            if first[left_pos] <= second[right_pos]:
                merged_numbers[merge_pos_false] = first[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos_false] = second[right_pos]
                right_pos += 1
            merge_pos_false = merge_pos_false + 1

        # If left partition is not empty, add remaining elements to merged numbers
        while left_pos <= j:
            merged_numbers[merge_pos_false] = first[left_pos]
            left_pos += 1
            merge_pos_false += 1

        # If right partition is not empty, add remaining elements to merged numbers
        while right_pos <= k:
            merged_numbers[merge_pos_false] = second[right_pos]
            right_pos = right_pos + 1
            merge_pos_false = merge_pos_false + 1

        return merged_numbers

    else:

        while left_pos <= j and right_pos <= k:
            if first[left_pos] >= second[right_pos]:
                merged_numbers[merge_pos_false] = first[left_pos]
                left_pos += 1
            else:
                merged_numbers[merge_pos_false] = second[right_pos]
                right_pos += 1
            merge_pos_false = merge_pos_false + 1

        # If left partition is not empty, add remaining elements to merged numbers
        while left_pos <= j:
            merged_numbers[merge_pos_false] = first[left_pos]
            left_pos += 1
            merge_pos_false += 1

        # If right partition is not empty, add remaining elements to merged numbers
        while right_pos <= k:
            merged_numbers[merge_pos_false] = second[right_pos]
            right_pos = right_pos + 1
            merge_pos_false = merge_pos_false + 1

        return merged_numbers


def insertion_sort(unsorted, reverse):
    """
    FINISHED
    :param unsorted: unsorted list
    :param reverse: boolean for reverse
    :return: return sorted list
    """

    if reverse is False:

        for i in range(1, len(unsorted)):
            j = i

            # Insert num_list[i] into sorted part
            # stopping once num_list[i] in correct position
            while j > 0 and unsorted[j] < unsorted[j - 1]:
                # Swap num_list[j] and num_list[j - 1]
                temp = unsorted[j]
                unsorted[j] = unsorted[j - 1]
                unsorted[j - 1] = temp
                j -= 1

    else:

        for i in range(1, len(unsorted)):
            j = i

            # Insert num_list[i] into sorted part
            # stopping once num_list[i] in correct position
            while j > 0 and unsorted[j] > unsorted[j - 1]:
                # Swap num_list[j] and num_list[j - 1]
                temp = unsorted[j]
                unsorted[j] = unsorted[j - 1]
                unsorted[j - 1] = temp
                j -= 1

    return unsorted