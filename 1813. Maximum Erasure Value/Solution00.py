/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.84 %
    Runtime : 2488 ms
    Memory Usage : 24.5 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 18.23 % of python3 submissions.
        Your memory usage beats 99.95 % of python3 submissions.
}
*/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1: return nums[0]
        sett = set()
        right = l-1
        left = l-1
        m = 0
        maxx = 0
        while left>-1:
            if nums[left] not in sett:
                m+=nums[left]
                sett.add(nums[left])
                left-=1
                maxx = max(maxx,m)
            else:
                m-=nums[right]
                sett.remove(nums[right])
                right-=1
                nums.pop()
        return maxx
            
            
        
        