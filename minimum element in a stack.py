class minelement:

    def __init__(self):
        self.minvalue = []
        self.stack = []

    def push(self, value):
        self.value = value
        if len(self.stack) == 0:
            self.minvalue.append(self.value)
            self.stack.append(self.value)

        elif self.value < self.minvalue[-1]:
            self.minvalue.append(self.value)
            self.stack.append(self.value)

        else:
            self.stack.append(self.value)

    def pop(self):
        if self.stack[-1] == self.minvalue[-1]:
            self.minvalue.pop()
            self.stack.pop()
        else:
            self.stack.pop()

    def get_min(self):
        return self.minvalue[-1]

    def get_list(self):
        return self.stack


result = minelement()
result.push(5)
print(result.get_list())
print(result.get_min())
result.push(3)
print(result.get_list())
print(result.get_min())
result.push(6)
print(result.get_list())
print(result.get_min())
result.push(1)
print(result.get_list())
print(result.get_min())
result.push(2)
print(result.get_list())
print(result.get_min())
result.push(7)
print(result.get_list())
print(result.get_min())
