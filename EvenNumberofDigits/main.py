# Given an array nums of integers, return how many of them contain an even number of digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2 == 0:
                print(i)
                count+=1
        return count