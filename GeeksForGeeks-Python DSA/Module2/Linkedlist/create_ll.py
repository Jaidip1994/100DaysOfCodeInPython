class LinkedList():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def print_link(head):
    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")

head = LinkedList(20)
head.next = LinkedList(30)
head.next.next = LinkedList(40)

print_link(head)