def binarysearch(list, key):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [1, 3, 5, 7, 9, 11]
key = 5
index = binarysearch(arr, key)
print(index)  # Output: 2
