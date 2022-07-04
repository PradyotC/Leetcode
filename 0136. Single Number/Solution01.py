/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 339 ms
    Memory Usage : 16.5 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 15.34 % of python3 submissions.
        Your memory usage beats 93.31 % of python3 submissions.
}
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        k = set()
        while nums:
            if nums[0] not in s: s.add(nums[0])
            else: k.add(nums[0])
            nums.pop(0)
        return tuple(s-k)[0]