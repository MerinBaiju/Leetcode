class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(nums[i] == target):
                return i
        for i in range(len(nums)):
            if(nums[i]>target):
                return i
        for i in range(len(nums)):
            if(nums[i]!=target):
                return len(nums)

        