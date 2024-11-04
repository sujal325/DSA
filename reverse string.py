def reverse(string):
    for i in string:
        list, index = [], -1
        for i in string:
            list.append(string[index])
            index -= 1
    reversed_string = "".join(list)
    print(reversed_string)


reverse("sujal")
