class Solution:
    def toLowerCase(self, str: str) -> str:
        newstring=""
        for i in str:
            if ord(i) in range(65,91):
                newstring+=chr(ord(i)+32)
            else:
                newstring+=i
        return newstring
    