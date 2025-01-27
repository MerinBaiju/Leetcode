class Solution(object):
    def removeDuplicates(self, nums):
        l,r=0,0
        while r<len(nums):
            c=0
            while r+1<len(nums) and nums[r]==nums[r+1]:
                r+=1
                c+=1
            for i in range(min(1,count)):
                nums[l]=nums[r]
                l+=1
            r+=1
        return l
        