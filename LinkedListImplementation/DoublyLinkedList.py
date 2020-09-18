class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        self.previous=None

class LinkedList:
    def __init__(self,val): 
        self.head = Node(val)
        self.tail = self.head
        self.length= 1

    # Append method
    def append(self, val):
        newnode = Node(val)
        newnode.previous=self.tail
        self.tail.next=newnode
        self.tail=newnode
        self.length+=1

    # Prepend method
    def prepend(self,val):
        newnode=Node(val)
        newnode.next=self.head
        self.head.previous=newnode
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
            self.head.previous=None

        # if given index is the last index or out of boundary
        elif index >= self.length-1:
            targetnode=self.traversetoIndex(self.length-1)
            targetnode.previous.next=None
            self.tail=targetnode.previous

        # If given index is something in between
        else:
            targetnode=self.traversetoIndex(index)
            targetnode.previous.next= targetnode.next
            targetnode.next.previous= targetnode.previous
        
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
            newnode=Node(val) # Create new node
            beforenode=self.traversetoIndex(index-1) # Traverse to the node at index -1
            
            newnode.next=beforenode.next # link this new node to the node at the index
            newnode.previous=beforenode # link this new node to the previous node 
            beforenode.next.previous=newnode 
            beforenode.next=newnode # Link this current node to the new node
            self.length+=1
 

    # Print method
    def printLinkedList(self):
        node=self.head
        while True:
            if node != None:
                previous = lambda node : str(node.previous.val) if node.previous else "None"
                next = lambda node : str(node.next.val) if node.next else "None"
                print(f"{node.val}, previous: {previous(node)}, next: {next(node)}")
                node=node.next
            else:
                break
            
myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.append(4)
myLinkedList.prepend(0)
myLinkedList.insert(3,3)
myLinkedList.remove(3)
myLinkedList.printLinkedList()

print("\nLength is: " ,myLinkedList.length)

print("head is: ", myLinkedList.head.val)

print("tail is: ", myLinkedList.tail.val)


