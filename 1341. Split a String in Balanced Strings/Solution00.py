/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 84.49 %
    Runtime : 24 ms
    Memory Usage : 13.9 MB
    Testcase : 40 / 40 passed
    Ranking : 
        Your runtime beats 98.97 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i = 0
        c_r = 0
        c_l = 0
        c = 0
        j = len(s)
        while i<j:
            if s[i]=="R":
                c_r += 1
            else:
                c_l += 1
            if (c_r>0 or c_l>0) and c_r==c_l:
                c += 1
                c_r = 0
                c_l = 0
            i+=1
        return c