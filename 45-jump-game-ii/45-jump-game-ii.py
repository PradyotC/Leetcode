class Solution:
    def jump(self, nums: List[int]) -> int:
        k = len(nums)-1
        ans = [0]+[pow(10,4) for i in range(k)]
        for i in range(k):
            a = ans[i]+1
            for j in range(1,nums[i]+1):
                if i+j>k: break
                if a >= ans[i+j]: continue
                ans[i+j] = a
            # print(ans)
        return ans[-1]
                