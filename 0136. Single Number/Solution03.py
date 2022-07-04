/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 298 ms
    Memory Usage : 17 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 18.63 % of python3 submissions.
        Your memory usage beats 10.53 % of python3 submissions.
}
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        k = set()
        while nums:
            if nums[0] not in s: s.add(nums.pop(0))
            else: k.add(nums.pop(0))
        return tuple(s-k)[0]