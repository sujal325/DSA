class stack:
    def __init__(self, list=None):
        if list == None:
            self.list = []
        else:
            self.list = list

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            print("list is empty")
        else:
            self.list.pop()

    def is_empty(self):
        return len(self.list) == 0

    def __str__(self):
        return str(self.list)


list = [1, 4, 5, 6, 3, 6, 4, 7, 8]
my_stack = stack(list)
my_stack.push(7)
print(my_stack)
my_stack.pop()
print(my_stack)
my_stack.is_empty()
isempty = my_stack.is_empty()
print(isempty)
