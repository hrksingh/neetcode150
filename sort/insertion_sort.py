from typing import List


def insertion_sort(arr: List) -> None:
    for i in range(1, len(arr)):
        temp = arr[i]  # element to be placed at the correct position
        j = i - 1  # start comparing from the left side of 'temp'

        # go from right-to-left(<-) and check if temp is less j element
        while j >= 0 and temp < arr[j]:
            # keep shifting elements if they are greater than temp this way large elements will move to right side and small element to left side
            arr[j + 1] = arr[j]
            j -= 1

        # When we either:
        #   (a) reach the beginning (j < 0), OR
        #   (b) find a smaller/equal element (temp >= arr[j]),
        # place 'temp' right after it -> at position 'j + 1'.
        arr[j + 1] = temp


if __name__ == "__main__":
    data = [-2, 45, 0, 11, -9]
    print("original:", data)
    insertion_sort(data)
    print("sorted:  ", data)
