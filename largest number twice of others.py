def largest(list):
    my_set = set()
    index = 0
    big = list[0]
    second_big = list[0]
    for i in list:
        if i >= big:
            big = i
            index_is = index
        index += 1
    for i in list:
        if i >= second_big and i < big:
            second_big = i
    if i > (second_big * 2):
        print(index_is)
    else:
        print(-1)


list = [1, 4, 2, 3, 0, 9, 0]
largest(list)
