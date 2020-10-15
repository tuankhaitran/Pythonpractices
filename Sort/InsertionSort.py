number =[99,44,6,2,1,4,63,87,283,4,0]


def InsertionSort(nums):
    newlist=[]
    
    for i in range(0,len(nums)):
        print(nums[i])
        if nums[i]< nums[0]:
            temp=nums.pop(i)
            nums.insert(0,temp)
        else:
            for j in range(0,i):
                if nums[i]<nums[j]:
                    nums.insert(j,nums.pop(i))

        print(nums)

               
InsertionSort(number)