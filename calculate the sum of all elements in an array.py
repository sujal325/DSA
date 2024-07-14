import array


def sum_of_elements(arr):
    sum = 0
    for i in arr:
        sum += i
    print(sum)


arr = array.array("i", [1, 4, 3, 5, 3])
sum_of_elements(arr)
