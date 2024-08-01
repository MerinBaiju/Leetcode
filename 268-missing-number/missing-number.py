class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        for i in nums:
            s+=i
        print(s)
        d=(len(nums)*(len(nums)+1))//2
        print(d)
        return d-s