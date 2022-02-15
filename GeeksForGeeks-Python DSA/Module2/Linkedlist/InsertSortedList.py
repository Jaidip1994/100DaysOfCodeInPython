class LinkedList():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


# Solution 1
# def insertList(head, val):
#     cur = nxt = temp = None
#     if not head:
#         return LinkedList(val)
#     if val < head.val:
#         temp = LinkedList(val)
#         temp.next = head
#         head = temp
#         return head
#     cur = head
#     nxt = cur.next
#     while nxt:
#         if cur.val < val < nxt.val:
#             temp = nxt
#             cur.next = LinkedList(val)
#             cur.next.next = temp
#             return head
#         cur = cur.next
#         nxt = nxt.next
#     cur.next = LinkedList(val)
#     return head


# Solution 2
def insertList(head, val):
    temp = LinkedList(val)
    if not head:
        return temp
    elif val < head.val:
        temp.next = head
        return temp
    else:
        cur = head
        while cur.next and cur.next.val < val:
            cur = cur.next
        temp.next = cur.next
        cur.next = temp
        return head


def print_link(head):
    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")


head = LinkedList(20)
head.next = LinkedList(30)
head.next.next = LinkedList(40)

# temp = insertList(head, 10)
# temp = insertList(head, 45)
temp = insertList(head, 25)
print_link(temp)
