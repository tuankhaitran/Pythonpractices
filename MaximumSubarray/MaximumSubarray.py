def maxSubArray(self, nums) -> int:
        su=nums[0];
        ma=nums[0];
        
        for i in range(1,len(nums)):
            su = max(su + nums[i], nums[i]);
            ma = max(ma,su);
            
        return ma;

    
