import array

arr = array.array("i", [9, 8, 1, 7, 5, 3, 2])
p = arr[0]
n = 0
z = len(arr)
for i in arr:
    if i <= p:
        p = i
        n += 1
    else:
        continue
if z == n:
    print("This is decreasing array.")
else:
    print("This is non-decreasing array.")
