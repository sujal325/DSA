import array

arr = array.array("i",[1,2,3,4,6,7,2,5,6,7,8,9,4,3,2,3,5,],)
p = arr[0]
for i in arr:
    if i > p:
        p = i
    else:
        continue
q = arr[0]
for i in arr:
    if i < p and i > q < p:
        q = i
    else:
        continue
print(f"{q} is the second largest and {p} is the largest integer in array.")
