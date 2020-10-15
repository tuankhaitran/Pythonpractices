number =[99,44,6,2,1,4,63,87,283,4,0]
def bubblesort(nums):
    outer=len(nums)-1
    inner=0
    while(outer>0):
        while(inner<outer):
            if(nums[inner]>nums[inner+1]):
                temp=nums[inner]
                nums[inner]=nums[inner+1]
                nums[inner+1]=temp                
            inner+=1
        outer-=1
        inner=0
    return nums
print(bubblesort([]))



