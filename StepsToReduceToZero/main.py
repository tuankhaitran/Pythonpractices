num=14
steps=0
while num >0:
    num = num / 2 if num%2==0 else num - 1
    steps+=1
print(num)
print(steps)
