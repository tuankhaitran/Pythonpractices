# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

# You can move according to the next rules:

# In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.


# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         pass


# The idea is to use the max() function in python which returns the max number out of the list
# We calculate the difference between x values of points[1] and points[0] and also the difference between y values
# For example [1,1] to [3,4] need 3-1= 2 steps on x axis and 4-1 = 3 steps on y axis. So that means, it will take at least 3 steps to reach from [1,1] to [3,4] with 2 diagonal steps and 1 horizontal or vertical step
# We continue to do this for the next pair of points. To do this, we can pop out the first element of the array

points=[[1,1],[3,4],[-1,0]]
totalsteps=0
min=0
while len(points)>1:       
    xdiff=abs(points[1][0]-points[0][0])
    ydiff=abs(points[1][1]-points[0][1])
    print(xdiff)
    print(ydiff)
    min+= max(xdiff,ydiff)
    print(min)
    points.pop(0)

