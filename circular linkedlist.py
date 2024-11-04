class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:  # List is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node  # Update the old tail to point to the new head
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # List is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

    def add_at_middle(self, data, position):
        if position <= 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1

        new_node.next = current.next
        current.next = new_node

        if new_node.next == self.head:  # Update tail if added at the end
            self.tail = new_node

    def delete_at_beginning(self):
        if not self.head:
            return

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:  # Find the node before tail
                current = current.next
            current.next = self.head
            self.tail = current

    def delete_at_middle(self, position):
        if position < 0:
            return

        if position == 0:
            self.delete_at_beginning()
            return

        current = self.head
        count = 0

        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1

        if current.next == self.head:  # If position is out of bounds
            return

        if current.next == self.tail:  # If deleting the tail
            current.next = self.head
            self.tail = current
        else:
            current.next = current.next.next

    def display(self):
        if not self.head:
            return "List is empty."

        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result


# Create a circular linked list
cll = CircularLinkedList()

# Add elements at the beginning
cll.add_at_beginning(10)
cll.add_at_beginning(20)

# Add elements at the end
cll.add_at_end(30)
cll.add_at_end(40)

# Add element at the middle
cll.add_at_middle(25, 1)  # Adding 25 at position 1 (after 20)

# Display the list
print(cll.display())  # Output: [20, 25, 10, 30, 40]

# Delete elements from the beginning
cll.delete_at_beginning()
print(cll.display())  # Output: [25, 10, 30, 40]

# Delete elements from the end
cll.delete_at_end()
print(cll.display())  # Output: [25, 10, 30]

# Delete element from the middle
cll.delete_at_middle(1)  # Deleting element at position 1
print(cll.display())  # Output: [25, 30]
