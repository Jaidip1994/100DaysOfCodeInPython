'''
Given a linked list of size n, you have to find whether the given linked list is sorted or not.
The sorting can either be non-increasing or non-decreasing.

Example 1:

Input:
LinkedList: 5->5->6->7->8
Output: 1
Example 2:

Input:
LinkedList: 2->5->7->8->99->7
Output: 0
Your Task:
The task is to complete the function isSorted() which takes head reference as argument. The function returns true if the LL is sorted, else it returns false. (The driver code prints 1 when the returned value is true, otherwise 0)

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= number of nodes <= 103
'''

# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


def isSorted(head):
    # code here
    if not head or not head.next:
        return 1
    res1 = res2 = False
    cur = head
    while cur and cur.next:
        if cur.data < cur.next.data:
            res1 = True
            break
        cur = cur.next

    cur = head
    while cur and cur.next:
        if cur.data > cur.next.data:
            res2 = True
            break
        cur = cur.next
    if res1 and res2:
        return 0
    else:
        return 1

# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB


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


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):

        n = int(input())
        arr = [int(x) for x in input().split()]

        ll = Llist()
        tail = None

        for nodeData in arr:
            tail = ll.insert(nodeData, tail)

        res = isSorted(ll.head)
        print(res)
# } Driver Code Ends
