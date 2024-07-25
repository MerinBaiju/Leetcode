class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        r=x[::-1]
        print(r)
        if(r==x):
            return True
        return False
        