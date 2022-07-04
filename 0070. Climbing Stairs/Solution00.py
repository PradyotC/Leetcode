/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 51.34 %
    Runtime : 45 ms
    Memory Usage : 14 MB
    Testcase : 45 / 45 passed
    Ranking : 
        Your runtime beats 50.46 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0,1]
        while n>1:
            ans.insert(1,ans.pop(0))
            ans[1] = sum(ans)
            n-=1
        return sum(ans)