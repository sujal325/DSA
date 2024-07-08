import array

arr = array.array("i", [])
while True:
    e = int(input("Type 0 for exit and 1 for add new integer: "))
    if e == 1:
        integer = int(input("Add integer: "))
        arr.append(integer)
    elif e == 0:
        break
    else:
        continue
addition = 0
for element in arr:
    addition += element
print(f"sum of array of integer is: {addition}")
