class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtMiddle(self, val):
        if not self.head:
            self.head = Node(val)
        
        new_code = Node(val)
        slow = self.head
        fast = self.head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new_code.next = slow.next
        slow.next = new_code
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end="-->")
            temp = temp.next
        print("None")

ll = Linklist()
# ll.insertAtBegin(5)
ll.insertAtBegin(4)
ll.insertAtBegin(2)
ll.insertAtBegin(1)

ll.insertAtMiddle(3)
ll.display()