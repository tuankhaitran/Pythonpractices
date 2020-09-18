class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self,val): 
        self.head = Node(val)
        self.tail = self.head
        self.length= 1
    # Append method
    def append(self, val):
        newnode = Node(val)
        self.tail.next=newnode
        self.tail=newnode
        self.length+=1

    # Prepend method
    def prepend(self,val):
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.length+=1

    # Traverse method
    def traversetoIndex(self,index):
        loopnode=self.head
        for i in range(index):
            loopnode=loopnode.next
        return loopnode

    # remove method
    def remove(self,index):
        # if index is 0
        if index==0:
            self.head=self.head.next

        # if given index is out of boundary
        elif index >= self.length-1:
            nodebefore=self.traversetoIndex(self.length-2)
            nodebefore.next=None
            self.tail=nodebefore

        # If given index is something in between
        else:
            nodebefore=self.traversetoIndex(index-1)
            nodebefore.next= nodebefore.next.next
        
        self.length-=1

    # Insert medthod
    def insert(self,index,val):
        # Case where we insert at the first and last of the linkedlist
        if index == 0:
            self.prepend(val)
        
        elif index > self.length-1: # if index larger than the list size, just append
            self.append(val)

        # Other cases
        else:
            currentnode=self.traversetoIndex(index-1) # Traverse to the node at index -1
            newnode=Node(val) # Create new node
            newnode.next=currentnode.next # link this new node to the node at the index
            currentnode.next=newnode # Link this current node to the new node
            self.length+=1

    # Reverse method
    # 0-1-2-3-4-5
    def swithchoroo(self,node):
        # if it has reach list end
        if node.next is None:
            # reassign the linkedlist head
            self.head=node
            return node

        # Reverse the rest list
        self.swithchoroo(node.next)
        # Put first element at the end
        node.next.next=node
        node.next=None
        return node

    def reverse(self):
        self.tail=self.swithchoroo(self.head)
        

    # Print method
    def printLinkedList(self):
        node=self.head
        while True:
            
            if node != None:
                next = lambda node : str(node.next.val) if node.next else "None"
                print(f"{node.val} next: {next(node)}")
                node=node.next
            else:
                break
            
myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(4)
myLinkedList.prepend(0)
myLinkedList.insert(3,3)
myLinkedList.append(5)

myLinkedList.reverse()
myLinkedList.printLinkedList()

print("\nLength is: " ,myLinkedList.length)

print("head is: ", myLinkedList.head.val)

print("tail is: ", myLinkedList.tail.val)


