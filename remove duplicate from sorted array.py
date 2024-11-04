def remove_duplicate(list):
    s = 0
    for f in range(0, len(list)):
        if list[f] != list[s]:
            s += 1
            list[s] = list[f]

    return list


list = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6]
k = remove_duplicate(list)
print(k)
