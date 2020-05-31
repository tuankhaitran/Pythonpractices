# Given two strings s and t , write a function to determine if t is an anagram of s.
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scounter=collections.Counter(s)
        tcounter=collections.Counter(t)
        return True if scounter==tcounter else False
      