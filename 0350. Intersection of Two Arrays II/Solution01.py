/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 55.19 %
    Runtime : 57 ms
    Memory Usage : 14 MB
    Testcase : 56 / 56 passed
    Ranking : 
        Your runtime beats 81.08 % of python3 submissions.
        Your memory usage beats 51.87 % of python3 submissions.
}
*/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rdict = {}
        for i in nums1:
            rdict[i]=rdict.get(i, 0)+1
        # print(rdict)
        ans = []
        for j in nums2:
            if j in rdict:
                rdict[j] -= 1
                if rdict[j]==0: del rdict[j]
                ans.append(j)
            # print(ans,rdict)
        return ans