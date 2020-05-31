# Say you have an array prices for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices) -> int:
        n=len(prices)
        profit=0
        for i in range(0,n-1):
            profit+=max([prices[i+1]-prices[i], 0 ])
        return profit
li=[7,1,5,3,6,4]


mysol=Solution()
print(mysol.maxProfit(li))