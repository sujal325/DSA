def reverse(list):
    reversed_list, reverse_order, i = [], -1, 0
    while i < len(list):
        reversed_list.append(list[reverse_order])
        i += 1
        reverse_order -= 1
    return reversed_list


list = [5, 4, 3, 2, 1, 0]
print(reverse(list))
