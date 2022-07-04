/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 34.67 %
    Runtime : 98 ms
    Memory Usage : 14.4 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 79.52 % of python3 submissions.
        Your memory usage beats 79.02 % of python3 submissions.
}
*/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = nums[0]
        opt,mopt = m1,m1
        for i in range(1,len(nums)):
            k = nums[i]
            opt,mopt = opt*k,mopt*k
            opt,mopt = max(opt,mopt,k),min(opt,mopt,k)
            m1 = max(m1,opt)
        return m1