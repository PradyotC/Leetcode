/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 34.67 %
    Runtime : 107 ms
    Memory Usage : 15.6 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 69.92 % of python3 submissions.
        Your memory usage beats 9.96 % of python3 submissions.
}
*/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        m1 = nums[0]
        opt = [m1 for i in range(l)]
        mopt = [m1 for i in range(l)]
        for i in range(1,l):
            k = nums[i]
            a,b = opt[i-1]*k,mopt[i-1]*k
            opt[i] = max(a,b,k)
            mopt[i] = min(a,b,k)
            m1 = max(m1,opt[i])
        return m1