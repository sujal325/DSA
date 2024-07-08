import array

arr = array.array(
    "i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
)
q = len(arr)
p = 0
n = arr[0]
for i in arr:
    if i >= n:
        n = i
        p += 1
    else:
        continue
if p == q:
    print("Array is sorted.")
else:
    print("Array is not sorted.")