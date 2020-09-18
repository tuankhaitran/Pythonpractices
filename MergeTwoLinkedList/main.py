# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        if l1==None:
            return l2
        elif l2==None:
            return l1
        
        if l1.val <= l2.val: 
            node=l1
            node.next=self.mergeTwoLists(node.next,l2)
            
        elif l1.val > l2.val:
            node=l2
            node.next=self.mergeTwoLists(node.next,l1)

        return node
        
li1=ListNode(1)
li1.next=ListNode(2)
li1.next.next=ListNode(4)

li2=ListNode(1)
li2.next=ListNode(3)
li2.next.next=ListNode(4)
mysol=Solution()

newli=mysol.mergeTwoLists(li1,li2)

nextli=newli.next
print(newli.next.next.val)