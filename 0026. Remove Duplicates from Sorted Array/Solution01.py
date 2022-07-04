/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.40 %
    Runtime : 207 ms
    Memory Usage : 15.5 MB
    Testcase : 361 / 361 passed
    Ranking : 
        Your runtime beats 16.13 % of python3 submissions.
        Your memory usage beats 60.62 % of python3 submissions.
}
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return
        if len(nums) == 0: return []
        sett = set()
        i = 0
        while i<len(nums):
            if nums[i] in sett:
                nums.pop(i)
            else:
                sett.add(nums[i])
                i+=1