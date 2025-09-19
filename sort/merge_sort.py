from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    Args:
        arr: A list of integers.

    Returns:
        A new list containing the sorted integers.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l_half = merge_sort(arr[:mid])
    r_half = merge_sort(arr[mid:])
    return merge(l_half, r_half)


def merge(left_arr: List[int], right_arr: List[int]) -> List[int]:
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left_arr: The left sorted list.
        right_arr: The right sorted list.

    Returns:
        A new, single sorted list containing elements from both inputs.
    """
    new = []
    i, j = 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            new.append(left_arr[i])
            i += 1
        else:
            new.append(right_arr[j])
            j += 1

    new.extend(left_arr[i:])
    new.extend(right_arr[j:])
    return new


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("original:", data)
    print("sorted:  ", merge_sort(data))
