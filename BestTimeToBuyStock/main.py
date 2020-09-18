# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# The idea is to find the min 
class Solution:
    def maxProfit(self, prices) -> int:
        maxprofit=0
        minprice=max(prices)
        for price in prices:
            if minprice > price:
                minprice=price
            maxprofit=max(maxprofit, price - minprice)
        return maxprofit


input= [7,1,5,3,6,4]

mysol=Solution()
print(mysol.maxProfit(input))