/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.19 %
    Runtime : 50 ms
    Memory Usage : 14.1 MB
    Testcase : 56 / 56 passed
    Ranking : 
        Your runtime beats 92.89 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rdict = {}
        for i in nums1:
            rdict[i]=rdict.get(i, 0)+1
        ans = []
        for j in nums2:
            if j in rdict:
                rdict[j] -= 1
                if rdict[j]==0: del rdict[j]
                ans.append(j)
        return ans