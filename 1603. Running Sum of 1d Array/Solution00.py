/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 90.48 %
    Runtime : 46 ms
    Memory Usage : 14.2 MB
    Testcase : 53 / 53 passed
    Ranking : 
        Your runtime beats 84.20 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)): nums[i]+=nums[i-1]
        return nums
        