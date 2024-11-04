class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_value(self, data, key):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        current = self.head
        while current:
            if current.data == key:
                if current == self.tail:
                    self.tail.next = new_node
                    new_node.prev = self.tail
                    self.tail = new_node
                    return

                else:
                    current.next.prev = new_node
                    new_node.next = current.next
                    current.next = new_node
                    new_node.prev = current
                    return

            current = current.next

    def del_head(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def del_value(self, value):

        if self.head is None:
            print("Empty list")
            return

        if self.head.data == self.tail.data == value:
            self.head = None
            self.tail = None
            return

        if self.head.data == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        if self.tail.data == value:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            return

        current = self.head
        while current:
            if current.data == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return

            current = current.next

        print("Value not found.")

    def transverse(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")


dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

# Traverse and display: 10 20 30
dll.transverse()
