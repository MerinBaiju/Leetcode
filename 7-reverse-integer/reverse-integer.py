class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r=0
        mi=-2**31
        ma=2**31-1
        o=abs(x)
        
        while o!=0:
            d=o%10
            r=r*10+d
            o=o//10
        
        if x>0 and r<=ma:
            
            return(r)
        elif x<0 and 0-r>=mi:
            return (-r)
        else:
            return 0
        