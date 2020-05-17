# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        '''
        Keep taking the number n and modulus to 10 each iteration, we will get each digits. 
        Also divide n to 10 for each iteration
        
        '''
        product = 1 
        sum=0
        while n > 0:
            product *= n%10
            sum += n%10
            n = int(n/10)
        return product-sum
