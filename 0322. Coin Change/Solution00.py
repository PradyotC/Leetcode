/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 40.85 %
    Runtime : 2698 ms
    Memory Usage : 14 MB
    Testcase : 188 / 188 passed
    Ranking : 
        Your runtime beats 24.01 % of python3 submissions.
        Your memory usage beats 96.74 % of python3 submissions.
}
*/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt = [float('inf')] * (amount+1)
        opt[0] = 0
        coins.sort()
        for i in range(1,amount+1):
            for j in coins:
                if j<=i:
                    opt[i] = min(opt[i],1 + opt[i-j])
        if opt[-1] == float('inf'):
            return -1
        else:
            return opt[-1]
        