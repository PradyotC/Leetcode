#Similiar to Q 121

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        l = 0
        r = 1
        while r < len(nums):
            # print(nums[r]-nums[l], nums[l], nums[r])
            if nums[r]<=nums[l]: 
                l = r
            else:
                ans = max(ans,nums[r]-nums[l])
            r+=1
        return ans