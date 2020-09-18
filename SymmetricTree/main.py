# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.checkMirror(root,root)
        
    def checkMirror(self,node1,node2):
        if node1==None and node2==None: 
            return True
        elif node1==None or node2==None: 
            return False
        
        
        return node1.val==node2.val and self.checkMirror(node1.left,node2.right) and self.checkMirror(node1.right,node2.left)

node=TreeNode(1)
node.left=TreeNode(2)
node.right=TreeNode(2)
node.left.left=TreeNode(3)
node.right.right=TreeNode(3)
mysol=Solution()
print(mysol.isSymmetric(node))
