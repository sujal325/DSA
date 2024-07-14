import array


def sorted_or_not(arr):
    len_of_array = len(arr)
    l = arr[0]
    len_of_array_after_check = 0
    for i in arr:
        if i >= l:
            l = i
            len_of_array_after_check += 1
        else:
            print("Array is not sorted.")
    if len_of_array == len_of_array_after_check:
        print("Array is sorted.")


arr = array.array("i", [1, 4, 2, 5, 6])
sorted_or_not(arr)
