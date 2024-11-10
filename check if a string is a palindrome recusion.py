def palindrome(sting):
    if len(sting) <= 1:
        return True
    if sting[0] == sting[-1]:
        return palindrome(sting[1:-1])
    else:
        return False


print(palindrome("ram"))
print(palindrome("madam"))
print(palindrome("bananab"))
