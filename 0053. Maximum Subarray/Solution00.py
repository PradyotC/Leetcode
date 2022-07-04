/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 49.65 %
    Runtime : 1250 ms
    Memory Usage : 28.1 MB
    Testcase : 209 / 209 passed
    Ranking : 
        Your runtime beats 27.81 % of python3 submissions.
        Your memory usage beats 21.74 % of python3 submissions.
}
*/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        opt = [0 for i in range(l)]
        opt[0] = m1 = nums[0]
        for i in range(1,l):
            opt[i] = max(opt[i-1],0)+nums[i]
            m1 = max(m1,opt[i])
        return m1
        