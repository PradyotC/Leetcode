/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 66.80 %
    Runtime : 71 ms
    Memory Usage : 14.4 MB
    Testcase : 294 / 294 passed
    Ranking : 
        Your runtime beats 32.38 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums.append(0)
        sum1 = sum(nums)
        left = 0
        right = sum1
        for i in range(len(nums)):
            right = right - nums[i]
            print(left,right)
            if left==right:
                break
            left = left + nums[i]
        if i==(len(nums)-1):
            i = -1
        return i