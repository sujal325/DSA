import array


def removing_duplicates(arr):
    unique_integer = []
    for i in arr:
        if i not in unique_integer:
            unique_integer.append(i)
    print(unique_integer)


arr = array.array("i", [1, 1, 1, 2, 4, 4])
removing_duplicates(arr)
