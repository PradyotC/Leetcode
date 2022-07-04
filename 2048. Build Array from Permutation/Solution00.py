/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 91.53 %
    Runtime : 205 ms
    Memory Usage : 14.6 MB
    Testcase : 140 / 140 passed
    Ranking : 
        Your runtime beats 34.48 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]