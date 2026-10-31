class Solution(object):
    def maxProfit(self, prices):
        minsofar = prices[0]
        profit = 0 

        for i in range(1,len(prices)):
             if prices[i] < minsofar :
                 minsofar = prices[i] 
             if prices[i] - minsofar > profit :
                profit = prices[i] - minsofar

        return profit 

        