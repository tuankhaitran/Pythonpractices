class Solution:
    def isHappy(self, n: int) -> bool:
        dupnum=[]
        while n!=1:
            dupnum.append(n) # To store numbers that are already appear
            a=str(n)
            total=0
            for i in a:
                total+=int(i)**2
            n=total    
            if n in dupnum:
                return False
        return True
            
            
            
            
mysol.Solution()
print(mysol.isHappy(19))