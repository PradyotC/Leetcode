class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        prof = 0
        for r in range(1,len(prices)):
            if prices[r]<prices[l]: l=r #Here when profit is negative means we have found the newest low point
            prof = max(prof,prices[r]-prices[l])
        return prof