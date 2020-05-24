# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node dataues up as the new dataue of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

# Class for a single node
class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None



# Binatry Tree Traversals
# Pre-order traversal (Print the current one then check left, if left has something than recursive function, if None then go to the right,)
    def preOrderTra(self,start,traversalstring=""):
        # Root -> left -> right
        if start:
            traversalstring += (str(start.val) + "-")
            traversalstring = self.preOrderTra(start.left,traversalstring)
            traversalstring = self.preOrderTra(start.right, traversalstring)
        return traversalstring

# In-order traversal (From current node go to the left, if left not null then go to the left again until its none. When left is None then print the current one then traverse to the right node)
    def inOrderTra(self,start,traversalstring=""):
        #  Left -> Root -> right
        if start:
            traversalstring=self.inOrderTra(start.left,traversalstring)
            traversalstring += (str(start.val) + "-")
            traversalstring=self.inOrderTra(start.right,traversalstring)
        return traversalstring

# post-order traversal 
    def postOrderTra(self,start,traversalstring=""):
        #  Left -> Right -> Root
        if start:
            traversalstring=self.postOrderTra(start.left,traversalstring)
            traversalstring=self.postOrderTra(start.right,traversalstring)
            traversalstring += (str(start.val) + "-")
        return traversalstring

           
# Print Binatry Tree by traversal options
def print_tree(node, traversal_type):
    if traversal_type=="preorder":
        print(node.preOrderTra(node, ""))
    elif traversal_type=="inorder":
        print(node.inOrderTra(node, ""))
    elif traversal_type=="postorder":
        print(node.postOrderTra(node, ""))
    else:
        print("'",traversal_type,"' traversal type is not supported")

#         1
#    2         3
#  4   5     6   7

tree = TreeNode(1)
tree.left=TreeNode(3)
tree.right=TreeNode(2)
tree.left.left=TreeNode(5)

tree2 = TreeNode(2)
tree2.left=TreeNode(1)
tree2.right=TreeNode(3)
tree2.left.right=TreeNode(4)
tree2.right.right=TreeNode(7)

print_tree(tree,"preorder")
print_tree(tree2,"preorder")


class Solution:
    def mergeTrees(self, t1, t2 ):
        t3=TreeNode()
        # If both of them is not null then we gonna add them together
        if t1 and t2:
            t3.val = t1.val+t2.val
            t3.left=self.mergeTrees(t1.left,t2.left)        
            t3.right=self.mergeTrees(t1.right,t2.right)

        # If t2 is null but t1 is not then assign t3.val to t1
        elif t1 and t2 == None:
            t3.val = t1.val 

        # If t1 is null but t2 is not then assign t3.val to t2
        elif t1 == None and t2:
            t3.val = t2.val 

        # if both of t1 and t2 are null then just return either t1 or t2
        else:
            return t2    
        return t3


mysol=Solution()
tree3=mysol.mergeTrees(tree,tree2)
print_tree(tree3,"preorder")


[1,2,null,3]
[1,null,2,null,3]