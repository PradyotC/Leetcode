class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        prof = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                prof = max(prof,prices[r]-prices[l])
            else: l=r #Here when profit is negative means we have found the newest low point
            r+=1
        return prof