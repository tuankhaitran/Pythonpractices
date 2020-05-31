# Reverse a singly linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1= ListNode(1)
node1.next=ListNode(2)

node1.next.next=ListNode(3)

node1.next.next.next=ListNode(4)

node1.next.next.next.next=ListNode(5)

class Solution:
    def reverseList(self, head) -> ListNode:
        result=None
        # The idea is each iteration we assign the current node to the result variable and the next node of result variable is the previous current node in the previous iteration
        while head:
            temp=head.next  # Assign head.next node to temp
            head.next=result # Assign the head.next node to result. Result variable will store the previous node in this line
            result=head # From this line the result now become the current node with the next node point to the previous node, which is the 'result' node from the previous iteration
            head=temp # Assign head node to temp because the temp.next point to the original next LinkedList node
        return result        


    def reverseList2(self, head) -> ListNode:
        if head==None or head.next==None:
            return head

        p=self.reverseList(head.next)

        head.next.next=head
        head.next=None
        return p

      
        
        return result
mysol=Solution()
print(mysol.reverseList2(node1).next.val)
