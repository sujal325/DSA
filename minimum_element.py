list_of_number = [1, 2, 4, 3, 5, 3, 6, 2]
l = 0
num = list_of_number[l]
for n in list_of_number:
    if n < num:
        num = n
    l += 1
print(num)
