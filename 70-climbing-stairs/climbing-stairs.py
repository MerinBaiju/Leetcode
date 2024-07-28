class Solution(object):
    def climbStairs(self, n):
        one,two=1,1
        for i in range(n-1):
            t=one
            one+=two
            two=t
        return one
        