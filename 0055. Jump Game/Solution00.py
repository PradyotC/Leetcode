/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.07 %
    Runtime : 497 ms
    Memory Usage : 15.2 MB
    Testcase : 170 / 170 passed
    Ranking : 
        Your runtime beats 92.99 % of python3 submissions.
        Your memory usage beats 82.43 % of python3 submissions.
}
*/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1] = len(nums)
        for i in range(nums[-1]):
            if nums[0]>=nums[-1]-1:
                return True
            if i<=nums[0]:
                nums[0] = max(nums[0],i+nums[i])
            else:
                return False
        return True