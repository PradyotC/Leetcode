/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.02 %
    Runtime : 531 ms
    Memory Usage : 25.9 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 73.62 % of python3 submissions.
        Your memory usage beats 72.28 % of python3 submissions.
}
*/

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        b1 = False
        for i in counts:
            if counts[i]>1:
                b1 = True
        return b1