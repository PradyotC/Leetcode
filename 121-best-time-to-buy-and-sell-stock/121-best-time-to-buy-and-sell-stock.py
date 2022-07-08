class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for r in range(1,len(prices)):
            if prices[r]<prices[0]: prices[0]=prices[r] #Here when profit is negative means we have found the newest low point
            prof = max(prof,prices[r]-prices[0])
        return prof