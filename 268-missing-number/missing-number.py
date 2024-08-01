class Solution(object):
    def missingNumber(self, nums):
        s=0
        for i in nums:
            s+=i
        d=(len(nums)*(len(nums)+1))//2
        return d-s