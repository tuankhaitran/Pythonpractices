# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next

node1= ListNode(1)
node2=node1.next=ListNode(2)

node1.next.next=ListNode(3)

node1.next.next.next=ListNode(4)

node1.next.next.next.next=ListNode(5)
mysol=Solution()
mysol.deleteNode(node2)

print(node1.next.val)