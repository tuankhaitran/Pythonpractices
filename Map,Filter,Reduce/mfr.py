import math
def area(r):
    return math.pi * (r**2)

# HOW TO CALCULATE AREAS FOR LOT OF CIRCLES ??
circlesr=[2,5,7.1,0.3,10]

#METHOD 1: DIRECT METHOD

print("\nMETHOD 1 ")
result1=[]
for r in circlesr:
    result1.append(area(r))

print(result1)
# METHOD 2: USE MAP FUNCTION
print("\nMETHOD 2 ")
result2= map(area,circlesr)
print(list(result2))

