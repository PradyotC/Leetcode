/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.24 %
    Runtime : 252 ms
    Memory Usage : 21.8 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 85.20 % of python3 submissions.
        Your memory usage beats 32.01 % of python3 submissions.
}
*/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1 for i in range(l)]
        for i in range(1,l):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(l-2,-1,-1):
            nums[i] *= nums[i+1]
            ans[i] *= nums[i+1]
        return ans