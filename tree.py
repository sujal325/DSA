class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key == data:
            return
        if data < self.key:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, value):
        if self.key == value:
            return True
        elif value < self.key:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def preorder(self):
        print(self.key, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.inorder()


root = BST(10)
numbers = [3, 7, 12, 15, 18, 22, 26, 31, 35, 39, 42, 47, 51, 55, 60, 64, 69, 73, 78, 82, 87, 91, 95, 100]
for i in numbers:
    root.insert(i)

root.preorder()  # Output should be: 10 3 7 12 15 18 22 26 31 35 39 42 47 51 55 60 64 69 73 78 82 87 91 95 100
print()  # To add a newline after preorder traversal

found = root.search(7)
print("Result:", found)  # Result: True

found = root.search(20)
print("Result:", found)  # Result: False

root.inorder()  # Output should be: 3 7 10 12 15 18 22 26 31 35 39 42 47 51 55 60 64 69 73 78 82 87 91 95 100
print()  # To add a newline after inorder traversal

#
