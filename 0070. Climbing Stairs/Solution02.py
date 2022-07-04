/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 51.34 %
    Runtime : 54 ms
    Memory Usage : 13.9 MB
    Testcase : 45 / 45 passed
    Ranking : 
        Your runtime beats 25.54 % of python3 submissions.
        Your memory usage beats 57.08 % of python3 submissions.
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
        return 1