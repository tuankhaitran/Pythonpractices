
def twoSum(self, nums: int, target: int):
    output=[]
    for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                 if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
        
    return output
                        
            