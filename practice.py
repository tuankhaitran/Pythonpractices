arr=[2,4,1,5,6,7]
arr2=[1]
arr3=[3,4,51,5,7,7,2]

def earliestRepeat(arr):
    # Create an empty dictionary
    mydict={}

    if len(arr) > 2:
        # Loop through array 
        for value in arr:
            # Check if value is already in the dictionary
            # If not already has
            if value not in mydict:
                mydict[value]= True
            # If already has
            else:
                return value
        # Cant find any repeat
        return "Not Found Repeat"
    else:
        return("No Repeat")

a=earliestRepeat(arr)
print(a)

