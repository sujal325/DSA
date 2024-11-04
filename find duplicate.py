def buplicate(list):
    the_set_of_planet_sujal = []
    for i in list:
        if i in the_set_of_planet_sujal:
            return i
        if i not in the_set_of_planet_sujal:
            the_set_of_planet_sujal.append(i)


list = [1, 2, 4, 3, 3, 5]
print(buplicate(list))
