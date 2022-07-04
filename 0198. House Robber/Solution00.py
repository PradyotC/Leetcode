/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 47.73 %
    Runtime : 40 ms
    Memory Usage : 13.9 MB
    Testcase : 68 / 68 passed
    Ranking : 
        Your runtime beats 72.43 % of python3 submissions.
        Your memory usage beats 65.68 % of python3 submissions.
}
*/

class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1:
            return nums[0]
        opt = [0 for i in range(l)]
        opt[0],opt[1] = nums[0],nums[1]
        m1 = max(opt)
        for i in range(2,l):
            for j in range(i-1):
                opt[i] = max(opt[i],opt[j])
            opt[i]+=nums[i]
            m1 = max(m1,opt[i])
        return m1