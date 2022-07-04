/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 40.16 %
    Runtime : 37 ms
    Memory Usage : 13.8 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 75.76 % of python3 submissions.
        Your memory usage beats 66.94 % of python3 submissions.
}
*/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k- 1).count('1') & 1

            