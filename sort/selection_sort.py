from typing import List


def selection_sort(arr: List[int]) -> None:
    size = len(arr)
    for i in range(size - 1):  # last element already in place
        min_index = i
        for j in range(min_index + 1, size):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:  # avoid swapping element with itself
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    selection_sort(data)
    print(data)
