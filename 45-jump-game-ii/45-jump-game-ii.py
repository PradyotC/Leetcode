class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [10001]*(n-1)+[0]
        for i in range(n-2,-1,-1):
            minn = min(n,nums[i]+i+1)
            for j in range(i+1,minn):
                if ans[j]<ans[i]: ans[i]=ans[j]
            ans[i] += 1
        return ans[0]
                