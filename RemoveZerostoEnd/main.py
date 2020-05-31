# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
import collections
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter=collections.Counter(nums)
        for i in range(counter[0]):
            nums.remove(0)
            nums.append(0)

input=[0,1,0,3,12]
mysol=Solution()
mysol.moveZeroes(input)
print(input)