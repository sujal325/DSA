import array


def moving_array(arr):
    list1 = array.array("i", [])
    list2 = array.array("i", [])
    for i in arr:
        if i > 0:
            list1.append(i)
        elif i == 0:
            list2.append(i)
        else:
            continue
    merge_arr = list1 + list2
    print(merge_arr)


arr = array.array("i", [1, 0, 3, 0, 0, 2, 5, 3])
moving_array(arr)
