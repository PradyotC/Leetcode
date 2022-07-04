/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.13 %
    Runtime : 63 ms
    Memory Usage : 14.1 MB
    Testcase : 150 / 150 passed
    Ranking : 
        Your runtime beats 47.86 % of python3 submissions.
        Your memory usage beats 95.67 % of python3 submissions.
}
*/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]