# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        i=0
        while i < len(nums):
            for j in range(nums[i]):
               result.append(nums[i+1])
            i+=2
        return result