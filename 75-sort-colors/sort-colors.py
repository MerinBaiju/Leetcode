class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[j]>nums[i]):
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
        return nums
        