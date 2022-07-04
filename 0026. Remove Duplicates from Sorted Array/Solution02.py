/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.40 %
    Runtime : 253 ms
    Memory Usage : 15.6 MB
    Testcase : 361 / 361 passed
    Ranking : 
        Your runtime beats 9.93 % of python3 submissions.
        Your memory usage beats 60.62 % of python3 submissions.
}
*/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return
        if len(nums) == 0: return []
        sett = set()
        i = 0
        j = 0
        k = len(nums)
        while j<k:
            if nums[i] in sett:
                nums.pop(i)
            else:
                sett.add(nums[i])
                i+=1
            j+=1