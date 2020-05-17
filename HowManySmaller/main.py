class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ''' Sorting the array in ascending order then the number or elements before it will be the number of smaller values. That number is also the index of the sorted array
        '''    
        result=[sorted(nums).index(i) for i in nums]
           
        return result