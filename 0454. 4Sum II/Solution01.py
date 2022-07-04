/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.16 %
    Runtime : 850 ms
    Memory Usage : 14.2 MB
    Testcase : 132 / 132 passed
    Ranking : 
        Your runtime beats 66.60 % of python3 submissions.
        Your memory usage beats 72.03 % of python3 submissions.
}
*/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        side1 = {}
        side2 = {}
        for i,a in enumerate(nums1):
            for j,b in enumerate(nums2):
                s = a+b
                if s not in side1: side1[s] = 1
                else: side1[s]+=1
        for i,a in enumerate(nums3):
            for j,b in enumerate(nums4):
                s = a+b
                if s not in side2: side2[s] = 1
                else: side2[s]+=1
        c = 0
        for k,v in side1.items():
            if -k in side2: c+=v*side2[-k]
        # print(side1)
        # print(side2)
        return c
        
# {-1: [(0, 0)], 0: [(0, 1), (1, 0)], 1: [(1, 1)]}
# {-1: [(0, 0)], 1: [(0, 1)], 2: [(1, 0)], 4: [(1, 1)]}
