/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.30 %
    Runtime : 295 ms
    Memory Usage : 15.5 MB
    Testcase : 43 / 43 passed
    Ranking : 
        Your runtime beats 27.66 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for item in nums:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1
        max_value = max(counts.values())
        [ans:=k for k,v in counts.items() if v==max_value and v>=(len(nums)//2)]
        return ans