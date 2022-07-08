#Similiar to Q 121

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        nums.append(-1)
        l = 0
        for r in range(1,len(nums)):
            if nums[r]<=nums[l]: l = r
            else: nums[-1] = max(nums[-1],nums[r]-nums[l])
        return nums[-1]