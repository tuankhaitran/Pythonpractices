
v = [2,-3,1]
v2 = [i * 4 for i in v]
print(v2) 

#Cartesian Product

A = [1,3,5,7]
B = [2,4,6,8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)