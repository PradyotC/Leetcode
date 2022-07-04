/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 32.54 %
    Runtime : 52 ms
    Memory Usage : 14 MB
    Testcase : 305 / 305 passed
    Ranking : 
        Your runtime beats 35.82 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        self.dictt = {0:1,1:x}
        def pw(b):
            if b in self.dictt: return self.dictt[b]
            p = b//2
            self.dictt[b] = pw(p)*pw(b-p)
            return self.dictt[b]
        if n < 0: return 1/pw(-n)
        return pw(n)
        