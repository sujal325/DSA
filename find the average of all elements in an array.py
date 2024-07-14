import array


def average(arr):
    l = 0
    n = len(arr)
    for i in arr:
        l += i
    av = l / n
    print(av)


arr = array.array("i", [1, 4, 3, 5, 6])
average(arr)
