class LinkedList():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        

def search(head, srch):
    count = 0
    while head:
        if head.val == srch:
            return True, count
        head = head.next
        count += 1
    return False, -1


head = LinkedList(20)
head.next = LinkedList(30)
head.next.next = LinkedList(40)

print(search(head, 40))