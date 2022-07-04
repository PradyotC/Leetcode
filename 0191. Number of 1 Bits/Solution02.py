/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.74 %
    Runtime : 43 ms
    Memory Usage : 13.8 MB
    Testcase : 601 / 601 passed
    Ranking : 
        Your runtime beats 63.31 % of python3 submissions.
        Your memory usage beats 50.28 % of python3 submissions.
}
*/

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum1 = 0
        while n>0:
            sum1+= n&1
            n = n>>1
        return sum1