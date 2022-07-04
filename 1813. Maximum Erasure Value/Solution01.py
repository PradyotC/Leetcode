/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.84 %
    Runtime : 1984 ms
    Memory Usage : 27.4 MB
    Testcase : 62 / 62 passed
    Ranking : 
        Your runtime beats 52.70 % of python3 submissions.
        Your memory usage beats 70.50 % of python3 submissions.
}
*/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1: return nums[0]
        sett = set()
        left = 0
        right = 0
        m = 0
        maxx = 0
        while right<l:
            if nums[right] not in sett:
                m+=nums[right]
                sett.add(nums[right])
                right+=1
                maxx = max(maxx,m)
            else:
                m-=nums[left]
                sett.remove(nums[left])
                left+=1
        return maxx
            
            
        
        