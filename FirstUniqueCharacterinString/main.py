# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=collections.Counter(s)
        for i,j in enumerate(a):
            if a[j]==1:
                return s.index(j)
        return -1
s= "leetcode"



mysol=Solution()
print(mysol.firstUniqChar(s))