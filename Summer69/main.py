# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.


def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False
                
        while not add:
            if num == 9:
                add=True
                break
            else:
                break
    return total            