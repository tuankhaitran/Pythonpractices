class Node:
    def __init__(self,val):
        self.val = val
        self.next=None
        
        
class Stack:
    def __init__(self):
        self.top = None
        self.bottom=None
        self.length=0
    def peek(self):
        return self.top
    def push(self,val):
        if (self.length==0):
            newnode=Node(val)
            self.top=newnode
            self.bottom=newnode
        else:
            newnode=Node(val)
            newnode.next= self.top
            self.top=newnode
        self.length+=1

    def pop(self):
        
        if (self.length==0):
            return None
        if(self.bottom==self.top):
            popnode=self.top
            self.bottom=None
            self.top=None
            self.length-=1
            return popnode

        else:
            popnode = self.top
            self.top = self.top.next
            self.length-=1
            return popnode
            
    def printStack(self):
            node=self.top
            while True:
                if node != None:
                    next = lambda node : str(node.next.val) if node.next else "None"
                    print(f"{node.val} next: {next(node)}")
                    node=node.next
                else:
                    break            
myStack=Stack()
myStack.push(1)
myStack.push(2)
myStack.pop()

myStack.pop()

myStack.printStack()
