class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        '''
        Use max function to find the largest number of candies
        add each amount of candies to the extraCandies and compare with the Largest Amount
        append true or false accordingly to the result list

        '''

        largestcandies=max(candies)
        for i in candies:
            if i + extraCandies >= largestcandies:
                result.append(True)
            else:
                result.append(False)
        return result

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))