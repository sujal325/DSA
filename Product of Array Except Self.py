def product(numbers):
    new_numbers_list = []
    for i in numbers:
        k = 1
        for j in numbers:
            if i == j:
                pass
            else:
                k *= j
        new_numbers_list.append(k)
    return new_numbers_list


list = [4, 2, 6, 3]
print(product(list))
