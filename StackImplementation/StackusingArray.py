
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


myStack= Stack()
myStack.printStack()
myStack.push(1)
myStack.push(2)
myStack.push(3)

print("Pop one: ", myStack.pop())

myStack.printStack()