"""

You are given a linked list of size n. You need to insert an element data just after the given position pos.
The position of first element is 1. If the given position is greater than n, then don't insert anything as it is not possible.

Example 1:

Input:
LinkedList: 1->2->3->4->5
position = 6, data = 10
Output: 1 2 3 4 5
Explanation: The given linked list is
1 2 3 4 5. The data 10 is to be inserted
after position 6. However, the linked
list only contains 5 elements so we
cannot insert the data.
Example 2:

Input:
LinkedList: 2->4->6->7->5->1->0
position = 7, data = 99
Output: 2 4 6 7 5 1 0 99
Your Task:
This is a function problem. You only need to complete the function insertAtPosition that takes head, pos, and data as parameters.  The printing is done automatically by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= n, pos <= 103

"""

#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def insertAtPosition(head,pos,data):
    #code here
    new_node = Node(data)
    temp = head
    pos -= 1
    while pos > 0 and temp.next:
        temp = temp.next
        pos -= 1
    if pos == 0:
        new_node.next = temp.next
        temp.next = new_node
        
            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]
        pos,data=[int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        insertAtPosition(ll.head,pos,data)
        printList(ll.head)
        print()