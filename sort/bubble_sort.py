from typing import List


def bubble_sort(arr):
    """In-place bubble sort (unoptimized). Mutates arr."""
    for i in range(len(arr) - 1):
        for j in range(
            len(arr) - i - 1
        ):  # we use -i as we want to skip last already sorted array elements
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def optimized_bubble_sort(arr: List[int]) -> None:
    """In-place bubble sort with early exit when already sorted."""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # tuple swap
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("original:", data)
    bubble_sort(data)
    print("sorted:  ", data)

    data2 = [1, 2, 3, 4, 5]
    print("original:", data2)
    optimized_bubble_sort(data2)
    print("sorted:  ", data2)
