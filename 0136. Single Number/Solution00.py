/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 325 ms
    Memory Usage : 17.1 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 16.02 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
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