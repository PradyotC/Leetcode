/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 45.36 %
    Runtime : 372 ms
    Memory Usage : 35.9 MB
    Testcase : 139 / 139 passed
    Ranking : 
        Your runtime beats 69.35 % of python3 submissions.
        Your memory usage beats 25.92 % of python3 submissions.
}
*/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def back(i,t):
            if i==len(nums): return 1 if t==target else 0
            if (i,t) in dp: return dp[(i,t)]
            dp[(i,t)] = back(i+1,t-nums[i])+back(i+1,t+nums[i])
            return dp[(i,t)]
        return back(0,0)