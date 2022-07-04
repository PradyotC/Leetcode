/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 51.34 %
    Runtime : 59 ms
    Memory Usage : 13.9 MB
    Testcase : 45 / 45 passed
    Ranking : 
        Your runtime beats 15.20 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1,2]
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        return a[n-1]
            
        