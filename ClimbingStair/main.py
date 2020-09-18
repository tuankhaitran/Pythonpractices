# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

def climbStairs(n: int) -> int:
    totalsteps=[1,1]
    
    for i in range(2,n+1):
        print(i)
        totalsteps.append(totalsteps[i-1]+totalsteps[i-2])
    print(totalsteps[-1])
    
climbStairs(4)