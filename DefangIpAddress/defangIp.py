class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

sol=Solution()
print(sol.defangIPaddr("255.100.50.0"))