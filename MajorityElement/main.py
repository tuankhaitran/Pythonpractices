# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.
import collections
class Solution:
    def majorityElement(self, nums) -> int:
        counter=collections.Counter(nums)
        
        return counter.most_common(1)[0][0]

li=[2,2,4,2,4,6,2,2]
mysol=Solution()
print(mysol.majorityElement(li))

