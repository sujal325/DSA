def merge(list1, list2):
    new_list, s, f = [], 0, 0
    while s < len(list1) and f < len(list2):
        if list1[s] < list2[f]:
            new_list.append(list1[s])
            s += 1

        else:
            new_list.append(list2[f])
            f += 1

    if s < len(list1):
        new_list.extend(list1[s:])

    if f < len(list2):
        new_list.extend(list2[f:])

    return new_list


list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge(list1, list2))
