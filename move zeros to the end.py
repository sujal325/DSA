def move_zeros(list):
    zeros_list = []
    non_zeros_list = []
    for i in list:
        if i == 0:
            zeros_list.append(i)
        else:
            non_zeros_list.append(i)
    new_list = non_zeros_list + zeros_list
    print(new_list)


list = [1, 2, 3, 0, 0, 0, 3, 4, 4, 5, 0]
move_zeros(list)
