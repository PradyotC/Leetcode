/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 34.67 %
    Runtime : 119 ms
    Memory Usage : 15.6 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 58.33 % of python3 submissions.
        Your memory usage beats 9.96 % of python3 submissions.
}
*/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        m1 = nums[0]
        opt = [m1 for i in range(l)]
        mopt = [m1 for i in range(l)]
        e,f = m1,m1
        for i in range(1,l):
            k = nums[i]
            a,b = e*k,f*k
            e = max(a,b,k)
            f = min(a,b,k)
            opt[i],mopt[i] = e,f
            m1 = max(m1,e)
        return m1