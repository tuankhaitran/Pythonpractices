# Given a string, find the length of the longest substring without repeating characters.

def lengofsubstring(self, text: str):
    mydict={}
    maxsofa=currmax=start=0
    for i, j in enumerate(text):
        