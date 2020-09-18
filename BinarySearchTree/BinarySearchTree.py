class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,val):
        # Create new node
        newnode=Node(val)
        # Case when we insert the very first node
        if self.root==None:
            self.root=newnode

        else:
            # Create loopnode to traverse through the tree
            loopnode = self.root
            # Begin traversing
            while True:
                # If less then go left
                if newnode.val < loopnode.val:
                    # If left has no node yet
                    if loopnode.left is None:
                        loopnode.left= newnode
                        break
                    else:
                        loopnode=loopnode.left
                # Larger then go right
                else:
                    # If right has no node yet:
                    if loopnode.right is None:
                        loopnode.right=newnode
                        break
                    else: 
                        loopnode=loopnode.right


    def lookup(self,val):
        currentnode=self.root
        # Start Traversing
        while True:
            # If current node is Null 
            if currentnode is None:
                print("This node not existed in the tree")
                return None
            else:
                # If given value is less than current node
                if val < currentnode.val:
                    currentnode= currentnode.left
                # If given value is larger than current node
                elif val > currentnode.val:
                    currentnode= currentnode.right
                # If given value is equal to the current node
                elif val == currentnode.val:
                    print("Found it")
                    return currentnode

    # preOrdertraversal Root - Left - Right
    def preOrderTraverse(self,node):
        if node is None:
            return None
        else:
            print(node.val)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)

    def traverse(self):  
        self.preOrderTraverse(self.root)  

    def remove(self,val):
        self.removeSupport(val,self.root)
    def removeSupport(self,val,root):
        
        parentNode=None
        currentNode=root

        # Traverse through the tree to find the target node
        while True:
            if currentNode==None:
                print("Node not existed")
                return None
            else: 
                if val < currentNode.val:
                    parentNode=currentNode
                    currentNode= currentNode.left
                elif val > currentNode.val:
                    parentNode=currentNode
                    currentNode= currentNode.right
                elif val == currentNode.val:
                    break

        # If parent node is None and
        if parentNode==None and currentNode.left is None and currentNode.right is None:
            currentNode=None
            return None

        # If the node is a leaf node then just make its parentNode point to None
        elif currentNode.left==None and currentNode.right==None:
            if currentNode == parentNode.left:
                parentNode.left=None
                
            elif currentNode == parentNode.right:
                parentNode.right=None
    
        # If the node have left subtree but does not have right sub tree
        # Make the parent node point to the root node of the sub tree
        elif currentNode.left==None and currentNode.right:
            if currentNode == parentNode.left:
                parentNode.left=currentNode.right
                
            elif currentNode== parentNode.right:
                parentNode.right=currentNode.right
            

        # If the node have right subtree but does not have left subtree
        # Make the parent node point to the root node of the sub tree
        elif currentNode.left and currentNode.right==None:
            if currentNode == parentNode.left:
                parentNode.left=currentNode.left
            elif currentNode== parentNode.right:
                parentNode.right=currentNode.left

        # If the node have both left and right subtree
        # Find the smallest node in the right subtree or largest in the left subtree
        else:
            # Loop to find smallest node in the right subtree
            smallestNode= currentNode.right
            while smallestNode.left:
                smallestNode=smallestNode.left
            # Now we want to copy the value of this node to the current node to make it become the successor
            currentNode.val= smallestNode.val
            # Now in our tree will have 2 node with the same value we want to delete the smallestNode.val
            
            # We can use recursion here, pass in the smallestNode.val and the root node of the right subtree
            currentNode.right=self.removeSupport(smallestNode.val, currentNode.right)

mytree =BinarySearchTree()
#          9
#    4          20
#  1   6      15  170
#           14    
mytree.insert(9)
mytree.insert(4)
mytree.insert(6)
mytree.insert(20)
mytree.insert(170)
mytree.insert(15)
mytree.insert(1)
mytree.insert(14)
print("Before")
mytree.traverse()

mytree.remove(4)
print("After")
mytree.traverse()

                    

