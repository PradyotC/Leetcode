/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 454 ms
    Memory Usage : 17.1 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 14.68 % of python3 submissions.
        Your memory usage beats 10.53 % of python3 submissions.
}
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        k = set()
        while nums:
            a = nums.pop(0)
            if a not in s: s.add(a)
            else: k.add(a)
        return tuple(s-k)[0]