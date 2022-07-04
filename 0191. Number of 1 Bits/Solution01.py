/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 62.74 %
    Runtime : 28 ms
    Memory Usage : 13.9 MB
    Testcase : 601 / 601 passed
    Ranking : 
        Your runtime beats 97.08 % of python3 submissions.
        Your memory usage beats 7.75 % of python3 submissions.
}
*/

class Solution:
    def hammingWeight(self, n: int) -> int:
        sum1 = 0
        while n>0:
            sum1+= n%2
            n = n//2
        return sum1