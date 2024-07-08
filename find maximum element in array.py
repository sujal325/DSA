import array

arr = array.array("i", [])
while True:
    cond = int(input("Type 0 for exit and any integer for add new element in array: "))
    if cond != 0:
        ele = int(input("New element: "))
        arr.append(ele)
        print(f"You appended {ele} in array {arr}")
    else:
        break
i = arr[0]
for element in arr:
    if element > i:
        i = element
    else:
        continue
print(f"Maximum element in array is {i}")
