# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1, nums2):
        nums1,nums2= (nums1,nums2) if len(nums1)<len(nums2) else (nums2,nums1)
        removelist=[]
        for i in nums1:
            if i in nums2:
                removelist.append(i)
                nums2.remove(i)
            
        return removelist

    def intersect2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1,p2=0,0
        result=[]
        while p1<len(nums1) and p2<len(nums2):
            num1=nums1[p1]
            num2=nums2[p2]
            if num1 < num2:
                p1+=1
            elif num2< num1:
                p2+=1
            else:
                result.append(num1)
                p1+=1
                p2+=1
        return result

nums1 = [5,0,0,6,1,6,2,2,4]
nums2 =[4,7,9,7,6,7]


mysol=Solution()

mysol.intersect2(nums1,nums2)