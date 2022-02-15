class LinkedList():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def reverseList(head):
    if not head or not head.next:
        return head
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

def print_link(head):
    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")


head = LinkedList(20)
head.next = LinkedList(30)
head.next.next = LinkedList(40)

temp = reverseList(head)
print_link(temp)