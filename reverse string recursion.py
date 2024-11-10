def reverse(string):
    if len(string) == 0:
        return ""

    else:
        return string[-1] + reverse(string[:-1])


print(reverse("fuck"))
