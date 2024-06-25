class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        out=[]
        for i in candies:
            if(i+extraCandies>=max(candies)):
                out.append(True)
            else:
                 out.append(False)
        return out
        
        