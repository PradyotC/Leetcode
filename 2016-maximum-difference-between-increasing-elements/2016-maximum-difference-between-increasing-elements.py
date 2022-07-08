#Similiar to Q 121

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        l = 0
        for r in range(1,len(nums)):
            if nums[r]<=nums[l]: l = r
            else: ans = max(ans,nums[r]-nums[l])
        return ans