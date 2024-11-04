def rotate_by_k(lst, k):
    k = k % len(lst)
    result = lst[-k:] + lst[:-k]
    return result


lst = [1, 2, 3, 4, 5, 6]
k = 3
rotated_list = rotate_by_k(lst, k)
print(rotated_list)
