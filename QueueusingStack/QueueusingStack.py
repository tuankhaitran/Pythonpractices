
# Class Stack
class Stack:
    def __init__(self):
        self.stack=[]
    
        self.length=0

    def peek(self):
        return self.top
    
    def push(self,val):
        self.stack.append(val)
        self.length+=1
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length==1:
            popone=self.stack.pop()
            self.length-=1
            return popone  
        else:
            popone=self.stack.pop()
            self.length-=1
            return popone

    def printStack(self):
        if (self.length==0):
            print("The stack is empty")
        else:
            print(self.stack)


# Class Queue 
class Queue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
        self.length=0
    
    def peek(self):
        pass

    def enqueue(self,val):
        self.stack1.push(val)
        self.length+=1

    def dequeue(self):
        if self.stack1.length==0 and self.stack2.length==0:
            return None
        if self.stack2.length==0:
            while(self.stack1.length!=0):
                self.stack2.push(self.stack1.pop())
        popone=self.stack2.pop()
        self.length-=1
        return popone

    def printQueue(self):
        self.stack1.printStack()
        self.stack2.printStack()
        pass

myque= Queue()
myque.enqueue(1)
myque.enqueue(2)
myque.enqueue(3)
myque.enqueue(4)
myque.enqueue(5)
print(myque.dequeue())
print(myque.dequeue())
print(myque.dequeue())
myque.enqueue(7)
print(myque.dequeue())

myque.printQueue()

     