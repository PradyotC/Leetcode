/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.64 %
    Runtime : 361 ms
    Memory Usage : 17.9 MB
    Testcase : 61 / 61 passed
    Ranking : 
        Your runtime beats 14.95 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set(nums)
        k = set(nums)
        i = 0
        while s and i<len(nums):
            if nums[i] in s: 
                s.remove(nums[i])
                nums.pop(i)
            else: i+=1
        return list(k-set(nums))[0]
        