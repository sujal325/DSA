import array

arr = array.array("i",[1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,2,5,5,5,5,5,5,5,5,5,5,5,])
find = int(input("Integer to find: "))
cout = 0
for element in arr:
    if element == find:
        cout += 1
    else:
        continue
print(f"This integer is {cout} in array.")