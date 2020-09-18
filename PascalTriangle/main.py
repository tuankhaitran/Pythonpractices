class Solution:
    def generate(self, numRows: int):
        result=[]
        for i in range(0,numRows):
            result.append([1]*(i+1))   # First fill everything with number 1
            if i >= 2:                  # Starting from when the numrows equal to 3 or more meaning index larger or equal 2. 
                for j in range(1,i):        # Reassign the corressponding index
                    result[i][j]=result[i-1][j-1]+result[i-1][j]
        return result
mysol=Solution()
print(mysol.generate(5))