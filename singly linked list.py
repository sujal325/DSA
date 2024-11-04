class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.tail = new_node
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, data, value):
        new_node = Node(data)
        current = self.head

        while current:
            if current.data == value:
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return

            current = current.next

        print("value not found.")

    def insert_before(self, data, value):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        if self.head.data == value:
            new_node.next = self.head
            self.head = new_node
            return

        while current:
            if current.next.data == value and current.next:
                new_node.next = current.next
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                return

            current = current.next

        print("value not found")

    def del_head(self):
        if self.head is None:
            print("This is empty list")
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def del_tail(self):
        if self.head is None:
            print("Empty list")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = None
        self.tail = current

    def del_value(self, value):
        if self.head is None:
            print("Empty list")
            return

        if self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next
        print("Value not found in list.")

    def transverse(self):
        current = self.head

        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def use(self):
        # Demonstrate the usage of linked list methods
        print("Inserting elements:")
        self.insert_beginning(10)
        self.insert_end(20)
        self.insert_end(30)
        self.insert_after(25, 20)
        self.insert_before(5, 10)
        self.transverse()  # Display list: 5 -> 10 -> 20 -> 25 -> 30 -> None

        print("\nDeleting head:")
        self.del_head()
        self.transverse()  # Display list: 10 -> 20 -> 25 -> 30 -> None

        print("\nDeleting tail:")
        self.del_tail()
        self.transverse()  # Display list: 10 -> 20 -> 25 -> None

        print("\nDeleting value 20:")
        self.del_value(20)
        self.transverse()  # Display list: 10 -> 25 -> None

        print("\nTrying to delete value 100 (not found):")
        self.del_value(100)  # Should print "Value not found in list."


# Usage
linked_list = LinkedList()
linked_list.use()