/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 69.50 %
    Runtime : 83 ms
    Memory Usage : 14.1 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 36.99 % of python3 submissions.
        Your memory usage beats 68.30 % of python3 submissions.
}
*/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))