'''
Given two Singly Linked List of N and M nodes respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have same data and with same arrangement too.

Example 1:

Input:
LinkedList1: 1->2->3->4->5->6
LinkedList2: 99->59->42->20
Output: Not identical 
Example 2:

Input:
LinkedList1: 1->2->3->4->5
LinkedList2: 1->2->3->4->5
Output: Identical
Your Task:
The task is to complete the function areIdentical() which takes the head of both linked lists as arguments and returns True or False.

Constraints:
1 <= N <= 103

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)
'''
# your task is to complete this function
# function should return true/1 if both
# are identical else return false/0
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
'''

#Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Code here
    while head1 or head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    if (not head1 and head2) or (not head2 and head1):
        return False
    return True

#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = node(val)
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        
def printList(head):
    while head:
        print(head.data, end=' ')
        head=head.next
    print()

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head2 = createList(arr, n)
        if(areIdentical(head1, head2)):
            print('Identical')
        else:
            print('Not identical')
