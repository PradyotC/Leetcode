/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 87.81 %
    Runtime : 37 ms
    Memory Usage : 13.9 MB
    Testcase : 255 / 255 passed
    Ranking : 
        Your runtime beats 79.23 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        [c:=c+1 for i in stones if i in set(jewels)]
        return c