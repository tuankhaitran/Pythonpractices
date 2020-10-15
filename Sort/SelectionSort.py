number =[99,44,6,2,1,4,63,87,283,4,0]

def SelectionSort(nums):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if (nums[j] < nums[i]):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums
print(SelectionSort(number))