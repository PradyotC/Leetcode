/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 49.95 %
    Runtime : 5832 ms
    Memory Usage : 14.3 MB
    Testcase : 54 / 54 passed
    Ranking : 
        Your runtime beats 25.13 % of python3 submissions.
        Your memory usage beats 13.94 % of python3 submissions.
}
*/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        opt = []
        m1 = 0
        for i in range(0,len(nums)):
            val = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    val = max(val,opt[j])
            opt.append(max(1,val+1))
            m1 = max(m1,opt[i])
        return m1