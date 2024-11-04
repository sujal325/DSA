def first(list, target):
    l, f = 0, len(list) - 1
    fo = -1

    while l <= f:
        mid = (l + f) // 2
        if list[mid] == target:
            fo = mid
            f = mid - 1
        elif list[mid] < target:
            l = mid + 1
        else:
            f = mid - 1

    return fo


def last(list, target):
    l, f = 0, len(list) - 1
    fo = -1

    while l <= f:
        mid = (l + f) // 2
        if list[mid] == target:
            fo = mid
            l = mid + 1
        elif list[mid] < target:
            l = mid + 1
        else:
            f = mid - 1

    return fo


list = [1, 2, 4, 4, 4, 4, 6, 7]
lastOccurance = last(list, 4)
firstOccurance = first(list, 4)

occurance = (lastOccurance - firstOccurance) + 1
print(occurance)
