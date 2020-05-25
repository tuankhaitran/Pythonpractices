# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Class for a node and also a Binary tree
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
        return traversalstring+str()

           
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

#         3
#    9         20
#            15   7

tree = TreeNode(3)
tree.left=TreeNode(9)
tree.right=TreeNode(20)
tree.right.left=TreeNode(15)
tree.right.right=TreeNode(7)

print_tree(tree,"postorder")

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return 1+ max(left,right)

mysol=Solution()
print(mysol.maxDepth(tree))