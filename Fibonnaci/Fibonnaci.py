# 0 1 1 2 3 5 8 13
def fibonacciRecursive(num):
    
    if num <2:
        return num
    
    result = fibonacciRecursive(num-1) + fibonacciRecursive(num-2)
    return result

def fibonacciLoop(num):
    if num < 2:
        return num
    else:
        store=[0,1]
        while num > 2:
            store= [store[1],store[1]+store[0]]
            num-=1
        return store[0]+store[1]

print(fibonacciRecursive(270))
print(fibonacciLoop(40))
