class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=[]
        l2=[]
        c=0
        for i in range(len(nums)-1):
            l1=nums[:i+1]
            s1=sum(l1)
            l2=nums[i+1:]
            s2=sum(l2)
            if abs(s1-s2)%2==0:
                c+=1
        return c

        