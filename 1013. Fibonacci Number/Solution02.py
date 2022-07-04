/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 68.34 %
    Runtime : 42 ms
    Memory Usage : 13.8 MB
    Testcase : 31 / 31 passed
    Ranking : 
        Your runtime beats 70.59 % of python3 submissions.
        Your memory usage beats 54.40 % of python3 submissions.
}
*/

class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        ans = [0,1]
        while n>2:
            ans.insert(1,ans.pop(0))
            ans[1] = sum(ans)
            n-=1
        return sum(ans)