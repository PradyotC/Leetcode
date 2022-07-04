/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 52.42 %
    Runtime : 144 ms
    Memory Usage : 15.5 MB
    Testcase : 742 / 742 passed
    Ranking : 
        Your runtime beats 99.42 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        sum1 = sum(nums)
        left = 0
        right = sum1
        for i in range(len(nums)):
            right = right - nums[i]
            if left==right:
                break
            left = left + nums[i]
        if i==(len(nums)-1):
            i = -1
        return i