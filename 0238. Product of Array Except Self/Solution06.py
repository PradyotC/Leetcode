/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.24 %
    Runtime : 232 ms
    Memory Usage : 21.6 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 96.42 % of python3 submissions.
        Your memory usage beats 33.65 % of python3 submissions.
}
*/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pr = [1 for i in range(l)]
        # pl = [1 for i in range(l)]
        ans = [1 for i in range(l)]
        # pl[0] = nums[0]
        pr[l-1] = nums[l-1]
        # for i in range(1,l):
        #     pl[i] = pl[i-1]*nums[i]
        for i in range(l-2,-1,-1):
            pr[i] = pr[i+1]*nums[i]
        ans[0] = pr[1]
        val = 1
        for i in range(1,l-1):
            val *= nums[i-1]
            ans[i] = val*pr[i+1]
        ans[l-1] = val*nums[l-2]
        return ans