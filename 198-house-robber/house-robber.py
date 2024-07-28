class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one,two=0,0
        for i in nums:
            t=max(i+one,two)
            one=two
            two=t
        return two

        