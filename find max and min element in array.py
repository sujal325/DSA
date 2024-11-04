def max_and_min(list):
    max_element, min_element = list[0], list[0]
    for i in list:
        if max_element < i:
            max_element = i
        elif min_element > i:
            min_element = i
    return max_element, min_element


list = [4, 2, 6, 7, 4, 3, 0]
print(max_and_min(list))
