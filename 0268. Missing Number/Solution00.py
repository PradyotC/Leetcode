/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.71 %
    Runtime : 159 ms
    Memory Usage : 15 MB
    Testcase : 122 / 122 passed
    Ranking : 
        Your runtime beats 77.43 % of python3 submissions.
        Your memory usage beats 98.31 % of python3 submissions.
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
            