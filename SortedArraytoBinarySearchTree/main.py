# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if len(nums)==0:
            return None
        return self.constructTree(nums,0,len(nums)-1)

    def constructTree(self, nums,left,right):
        if left>right:
            return None
        mid=int((left+right)/2)
        node=TreeNode(nums[mid])
        node.left=self.constructTree(nums,left,mid-1)
        node.right=self.constructTree(nums,mid+1,right)
        return node

li=[-10,-3,0,5,9]
mysol=Solution()
node=mysol.sortedArrayToBST(li)
print(node.val)