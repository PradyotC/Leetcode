class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [10001]*n
        ans[-1]=0
        for i in range(n-2,-1,-1):
            minn = min(n,nums[i]+i+1)
            for j in range(i+1,minn):
                ans[i] = min(ans[i],ans[j])
            ans[i] += 1
        return ans[0]
                