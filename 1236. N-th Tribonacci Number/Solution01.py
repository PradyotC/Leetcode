/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.17 %
    Runtime : 58 ms
    Memory Usage : 13.9 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 16.29 % of python3 submissions.
        Your memory usage beats 58.93 % of python3 submissions.
}
*/

class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        if n in range(0,3):
            return ans[n]
        for i in range(3,n):
            ans.insert(2,ans.pop(0))
            ans[-1] = sum(ans)
        return sum(ans)