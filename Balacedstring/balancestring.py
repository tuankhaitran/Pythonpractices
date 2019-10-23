def balancedStringSplit(s: str):
    countR,countL,count=0,0,0
    for i in range(len(s)):
        if s[i]=="R":
            countR+=1
        elif s[i]=="L":
            countL+=1
        if countL == countR:
            count+=1

    
    