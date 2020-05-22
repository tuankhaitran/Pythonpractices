# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.


# Class to create a single node, each node will have a value and a next node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Class LinkedList to connect nodes together to form a LinkedList
class LinkedList:
    # Default constructor
    def __init__(self):
        self.head=None

    # Function to change a list to LinkedList
    def initList(self,datalist):
        # Create head node
        self.head=ListNode(datalist[0])
        temp=self.head
        # Create node for every data
        for i in datalist[1:]:
            node = ListNode(i)
            temp.next = node
            temp=temp.next
        return temp

    def printlist(self):
        if self.head == None: return
        node = self.head
        while node != None:
            print(node.val,end=' ')
            node = node.next



class Solution:
    def getDecimalValue(self, head):
        temp, lenlist = head, 0
        while(temp): # while temp is true (has value)
            lenlist += 1
            temp=temp.next 
        intresult=0
        for i in range(lenlist):
            x=head.val
            intresult+=x*2**(lenlist-1-i)  # Multiply each digit with the appropriate power of 2. 
            head=head.next
        return intresult
        
mylist=LinkedList()
mylist.initList([1,0,2])
mysol=Solution()
mysol.getDecimalValue(mylist.head)

