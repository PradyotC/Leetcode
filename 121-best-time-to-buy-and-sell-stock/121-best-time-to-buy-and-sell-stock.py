class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        prof = 0
        for r in range(1,len(prices)):
            if prices[r]<low: low=prices[r] #Here when profit is negative means we have found the newest low point
            prof = max(prof,prices[r]-low)
        return prof