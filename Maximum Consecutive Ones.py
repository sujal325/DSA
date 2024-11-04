def consecutive_ones(list):
    count = 0
    for i in list:
        if i == 1:
            count += 1
        else:
            count = 0
    print(count)


list = [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
consecutive_ones(list)
