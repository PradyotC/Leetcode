/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.71 %
    Runtime : 3762 ms
    Memory Usage : 15.2 MB
    Testcase : 122 / 122 passed
    Ranking : 
        Your runtime beats 7.78 % of python3 submissions.
        Your memory usage beats 33.20 % of python3 submissions.
}
*/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = list(nums)
        for i in range(0,max(nums)+1):
            if i not in l:
                return i
        return max(nums)+1