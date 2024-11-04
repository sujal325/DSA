def palindrome(string1, string2):
    if len(string1) != len(string2):
        return print("It is not palindrome")
    setofstring1 = set(string1)
    setofstring2 = set(string2)
    for i in setofstring1:
        if i not in setofstring2:
            print("It is not palindrome")
            break
    for i in setofstring2:
        if i not in setofstring1:
            print("It is not palindrome")
            break
    print("It is a palindrome")


palindrome("python", "hence")
