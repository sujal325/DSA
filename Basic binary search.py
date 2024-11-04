def BS(list, target):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


list = [1, 2, 5, 6, 7, 9]
print(BS(list, 2))
