class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False] * (n-1) + [True] 
        for i in range(n-2,-1,-1):
            jump = min(n-1-i, nums[i])
            for j in range(1,jump+1):
                if ans[i+j]: 
                    ans[i]=True
                    break
        return ans[0]