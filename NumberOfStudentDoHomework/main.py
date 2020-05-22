# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        if len(startTime) != len(endTime):
            print("Start time and End Time length should be equal")
            return 0

        for i in range(len(startTime)):
            if startTime[i] > endTime[i]:
                print("Start time should be before End time ")
                return 0
            elif queryTime in range(startTime[i],endTime[i]+1):
                count += 1
        return count 

           