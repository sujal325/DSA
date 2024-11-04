class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def middle(self):
        slow ,fast = self.head,self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data