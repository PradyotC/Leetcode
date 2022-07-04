/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.24 %
    Runtime : 436 ms
    Memory Usage : 21.3 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 19.59 % of python3 submissions.
        Your memory usage beats 43.03 % of python3 submissions.
}
*/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [1 for i in range(l)]
        for i in range(1,l):
            ans[i] = ans[i-1] * nums[i-1]
        left = 1
        for i in range(l-2,-1,-1):
            print(nums[i+1],ans[i])
            left *= nums[i+1]
            ans[i] *= left
        return ans