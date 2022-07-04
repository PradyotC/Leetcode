/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 59.71 %
    Runtime : 49 ms
    Memory Usage : 13.9 MB
    Testcase : 283 / 283 passed
    Ranking : 
        Your runtime beats 99.77 % of python3 submissions.
        Your memory usage beats 75.94 % of python3 submissions.
}
*/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        opt = [0,0,min(cost[0],cost[1])]
        for i in range(3,len(cost)+1):
            opt.pop(0)
            opt.append(min(opt[0]+cost[i-2],opt[1]+cost[i-1]))
        return opt[-1]