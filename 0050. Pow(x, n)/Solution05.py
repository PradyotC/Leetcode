/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 32.54 %
    Runtime : 61 ms
    Memory Usage : 14 MB
    Testcase : 305 / 305 passed
    Ranking : 
        Your runtime beats 16.31 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.dictt = {0:1,1:x}
        def pw(b):
            if b in self.dictt: return self.dictt[b]
            p = b//2
            q = b-p
            self.dictt[b] = pw(p)*pw(q)
            return self.dictt[b]
        if n < 0: return 1/pw(-n)
        return pw(n)
        