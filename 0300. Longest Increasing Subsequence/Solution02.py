/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 49.95 %
    Runtime : 4013 ms
    Memory Usage : 14.2 MB
    Testcase : 54 / 54 passed
    Ranking : 
        Your runtime beats 51.67 % of python3 submissions.
        Your memory usage beats 46.77 % of python3 submissions.
}
*/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        opt = [1 for i in range(len(nums))]
        m1 = 0
        for i in range(0,len(nums)):
            val = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    val = max(val,opt[j])
            opt[i] = max(opt[i],val+1)
            m1 = max(m1,opt[i])
        return m1