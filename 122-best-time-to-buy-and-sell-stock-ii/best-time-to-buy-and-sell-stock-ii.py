class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        p=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                p+=(prices[i]-prices[i-1])
        return p

        