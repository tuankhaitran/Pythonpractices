class Solution:
    def reverse(self, x: int) -> int:
          
      

        if(x<0):
            newstring = str(x)[:0:-1]
            newstring= '-' + newstring
     
        else:
            newstring = str(x)[::-1]
          
        if(int(newstring,10)<=(-2)**31) or (int(newstring,10)>=2**31):    
            
            return 0
        else:
            return int(newstring,10)

