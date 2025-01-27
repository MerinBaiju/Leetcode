class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res,c=0,0
        for n in nums:
            if c==0:
                res=n
                c+=1
            elif n==res:
                c+=1
            else:
                c-=1
        return res
            
        