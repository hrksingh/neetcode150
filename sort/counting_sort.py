from typing import List


def count_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of non-negative integers using a stable counting sort algorithm.

    Args:
        arr: A list of non-negative integers.

    Returns:
        A new list containing the sorted elements.
    """
    # 0. Handle the edge case of an empty list.
    if not arr:
        return []

    # Find the maximum value to determine the size of the counter array.
    max_val = max(arr)

    # 1. Count frequencies of each element.
    # The size is max_val + 1 to accommodate the number max_val itself (e.g., for [0, 3], we need indices 0, 1, 2, 3).
    counter = [0] * (max_val + 1)
    for num in arr:
        counter[num] += 1

    # 2. Calculate cumulative sum to find the last position of each element.
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    # 3. Build the output array by iterating backwards from the input array.
    # This ensures the sort is "stable".
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        value = arr[i]
        position = counter[value] - 1
        output[position] = value
        counter[value] -= 1

    return output


if __name__ == "__main__":
    data = [2, 0, 2, 1, 1, 0, 4, 1, 3]
    print("original:", data)
    print("sorted:  ", count_sort(data))
    # Expected output: [0, 0, 1, 1, 1, 2, 2, 3, 4]
