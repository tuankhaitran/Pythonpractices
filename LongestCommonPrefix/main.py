class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
           return ""

        
        for i, letters in enumerate(zip(*strs)):
            print(letters)
            if len(set(letters)) > 1:
               return(strs[0][:i])
        else:
            return min(strs)

sol=Solution()
print(sol.longestCommonPrefix(["aa","a"]))
