/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 34.67 %
    Runtime : 145 ms
    Memory Usage : 15.7 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 33.51 % of python3 submissions.
        Your memory usage beats 8.35 % of python3 submissions.
}
*/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        opt = [nums[i] for i in range(l)]
        mopt = [nums[i] for i in range(l)]
        m1 = opt[0]
        for i in range(1,l):
            k = nums[i]
            a,b = opt[i-1]*k,mopt[i-1]*k
            opt[i] = max(a,b,k)
            mopt[i] = min(a,b,k)
            m1 = max(m1,opt[i])
        return m1