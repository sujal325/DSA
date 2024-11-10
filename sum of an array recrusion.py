def sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum(list[1:])


list = [1, 2, 5, 3, 4, 6]
print(sum(list))
