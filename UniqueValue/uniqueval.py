# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

class Solution:
    def singleNumber(self, nums) -> int:
        snums=sorted(nums)
        while len(snums) > 1 :
            if snums[0]!=snums[1]:
                return snums[0]
            else:
                snums.pop(0)
                snums.pop(0)
        else:
            return snums[0]


    def singleNumber2(self,nums) -> int:
        return 2*sum(set(nums)) - sum(nums)


nums=[1,7,3,4,3,4,1]
mysol=Solution()
print(mysol.singleNumber(nums))
print(mysol.singleNumber2(nums))