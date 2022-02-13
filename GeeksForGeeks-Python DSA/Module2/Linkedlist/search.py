class LinkedList():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        

def search(head, srch):
    while head:
        if head.val == srch:
            return True
        head = head.next
    return False


head = LinkedList(20)
head.next = LinkedList(30)
head.next.next = LinkedList(40)

print(search(head, 40))