def rotate(list, k):
    count = 1
    while count <= k:
        last = list.pop()
        list.insert((count - 1), last)
        count += 1
    print(list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotate(list, 4)
