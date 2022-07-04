/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 152 ms
    Memory Usage : 17.6 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 81.10 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        k = set()
        for i in nums:
            if i not in s: s.add(i)
            else: k.add(i)
        return tuple(s-k)[0]