import array


def minimum():
    arr = array.array("i", [7, 4, 3, 1, 5, 3, 6])
    l = arr[0]
    for i in arr:
        if i < l:
            l = i
        else:
            continue
    print(l)


minimum()
