def spy_game(nums):
    newlist=[]
    
    for n in nums:
        if n == 0 or n == 7:
            newlist.append(n)
   
    if newlist==[0,0,7]:
        return True
    else:
        return False