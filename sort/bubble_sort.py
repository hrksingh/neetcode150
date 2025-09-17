def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(
            len(arr) - i - 1
        ):  # we use -i as we want to skip last already sorted array elements
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def optimized_bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    arr = [-2, 45, 0, 11, -9]
    print(arr)
    bubble_sort(arr)
    print(arr)
