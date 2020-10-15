number =[99,44,6,2,1,4,63,87,283,4,0]


def MergeSort(nums):
    if len(nums)==1:
        return nums

    left = nums[0:int(len(nums)/2)]
    right = nums[int(len(nums)/2)::]
    print(left)
    print(right)
    return merge(MergeSort(left),MergeSort(right))

def merge(left, right):
    # Easy way
    # newarr=[]
    # newarr=sorted(left+right)

    # Other way
    newarr=[]
    leftIndex=0
    rightIndex=0
    
    while leftIndex < len(left) and rightIndex < len(right):  
        if left[leftIndex]<right[rightIndex]:
            newarr.append(left[leftIndex])
            leftIndex+=1
        else:
            newarr.append(right[rightIndex])
            rightIndex+=1

    return newarr + left[leftIndex::] + right[rightIndex::]

print(MergeSort(number))



    
