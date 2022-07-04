/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 37.65 %
    Runtime : 2242 ms
    Memory Usage : 27.9 MB
    Testcase : 93 / 93 passed
    Ranking : 
        Your runtime beats 25.13 % of python3 submissions.
        Your memory usage beats 76.19 % of python3 submissions.
}
*/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            # sum([left ,..., right]) = total - x
            current += nums[right]
            # if larger, move `left` to left
            while current > total-x and left <= right:
                current -= nums[left]
                left += 1
            # check if equal
            if current == total-x:
                maxi = max(maxi, right-left+1)

        return n-maxi if maxi != -1 else -1