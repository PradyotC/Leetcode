/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.02 %
    Runtime : 854 ms
    Memory Usage : 26.2 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 14.72 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         counts = Counter(nums)
#         b1 = False
#         for i in counts:
#             if counts[i]>1:
#                 b1 = True
#         return b1


#using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums)==len(set(nums)) else True