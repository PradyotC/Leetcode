/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.77 %
    Runtime : 703 ms
    Memory Usage : 27.2 MB
    Testcase : 51 / 51 passed
    Ranking : 
        Your runtime beats 77.73 % of python3 submissions.
        Your memory usage beats 73.78 % of python3 submissions.
}
*/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictt = {}
        for i in range(len(nums)):
            if nums[i] in dictt and (i-dictt[nums[i]])<=k: return True
            dictt[nums[i]]=i