from array import *

vals = array("i", [1, 2, 3, 4, 5])
a = 0
condi = 7
while True:
    condi = int(input("1 for continue and 0 for exit: "))
    if condi == 1:
        a = int(input("Integer you want to append: "))
        vals.append(a)
    elif condi == 0:
        break
    else:
        print("sorry we don't have that feature.")
print(vals)
