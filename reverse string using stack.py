def reverse(s):
    my_list = []
    for i in s:
        my_list.append(i)
    reversed_string = ""
    while my_list:
        reversed_string += my_list.pop()
    print(reversed_string)


value = input("Type string: ")
reverse(value)
