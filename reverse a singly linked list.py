# Node class to create nodes of the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Pointer to the next node
        self.tail = None  # Pointer to the next node


# LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head of the list

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} --> ", end="")
            current = current.next


# Driver code to test the reverse function
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)

    print(f"Original Linked List: {llist.print_list()}")  # Using f-string
    llist.reverse()
    print(f"Reversed Linked List: {llist.print_list()}") 
