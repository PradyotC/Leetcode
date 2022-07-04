/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 72.88 %
    Runtime : 90 ms
    Memory Usage : 14.3 MB
    Testcase : 288 / 288 passed
    Ranking : 
        Your runtime beats 74.96 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)

        ans = list(set1.intersection(set2).union(set2.intersection(set3)).union(set1.intersection(set3)))
        return ans
        