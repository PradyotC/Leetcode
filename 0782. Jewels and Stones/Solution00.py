/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 87.81 %
    Runtime : 46 ms
    Memory Usage : 13.9 MB
    Testcase : 255 / 255 passed
    Ranking : 
        Your runtime beats 53.18 % of python3 submissions.
        Your memory usage beats 58.03 % of python3 submissions.
}
*/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        [c:=c+1 for i in stones if i in set(jewels)]
        return c