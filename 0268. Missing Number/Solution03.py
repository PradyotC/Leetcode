/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.71 %
    Runtime : 240 ms
    Memory Usage : 15.3 MB
    Testcase : 122 / 122 passed
    Ranking : 
        Your runtime beats 34.74 % of python3 submissions.
        Your memory usage beats 33.20 % of python3 submissions.
}
*/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0]!=0: return 0
        m = nums[-1]+1
        nums[0]=1
        while nums[0]!=m:
            if nums[nums[0]]!=nums[0]:return nums[0]
            nums[0]+=1
        return nums[0]
            