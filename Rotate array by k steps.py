import array

arr = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
k = int(input("Steps you want to rotate: "))
q = arr[k:] + arr[:k]
print(q)
