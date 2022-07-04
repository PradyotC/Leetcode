/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.71 %
    Runtime : 235 ms
    Memory Usage : 15.3 MB
    Testcase : 122 / 122 passed
    Ranking : 
        Your runtime beats 36.86 % of python3 submissions.
        Your memory usage beats 15.08 % of python3 submissions.
}
*/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0]!=0: return 0
        m = nums[-1]
        i=0
        while i!=m+1:
            if nums[i]!=i:return i
            i+=1
        return i
            