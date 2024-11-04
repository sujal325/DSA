class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


# Create a linked list with a cycle
ll = LinkedList()
ll.push(3)
ll.push(2)
ll.push(1)

# Create a cycle for testing
ll.head.next.next.next = ll.head  # Linking last node to head to form a cycle

# Check for cycle
print(ll.detect_cycle())  # Output: True

# Create a linked list without a cycle
ll2 = LinkedList()
ll2.push(3)
ll2.push(2)
ll2.push(1)

# Check for cycle
print(ll2.detect_cycle())  # Output: False
