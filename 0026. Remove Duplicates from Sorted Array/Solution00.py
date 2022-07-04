/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.40 %
    Runtime : 153 ms
    Memory Usage : 15.7 MB
    Testcase : 361 / 361 passed
    Ranking : 
        Your runtime beats 42.44 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return
        if len(nums) == 0: return []
        # sett = set()
        # i = 0
        # while i<len(nums):
        #     if nums[i] in sett:
        #         nums.pop(i)
        #     else:
        #         sett.add(nums[i])
        #         i+=1
        k = sorted(list(set(nums)))
        nums.clear()
        nums+= k