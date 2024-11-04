class balanced_parentheses:
    def __init__(self, parentheses):
        self.paren = parentheses

    def check(self):
        count = 0
        for i in self.paren:
            if i == "(":
                count += 1
            elif i == ")":
                count -= 1
            if count < 0:
                print("False")
                return
        if count == 0:
            print("True")
        else:
            print("False")


parentheses1 = input("Type parentheses: ")
result = balanced_parentheses(parentheses1)
result.check()
