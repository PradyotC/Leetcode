/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.78 %
    Runtime : 74 ms
    Memory Usage : 14.5 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 52.71 % of python3 submissions.
        Your memory usage beats 34.65 % of python3 submissions.
}
*/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def retdict(r):
            rdict = {}
            for i in r:
                rdict[i]=rdict.get(i, 0)+1
            return rdict
        return retdict(s)==retdict(t)

#         dic = {}
#         for i in s:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
        
#         for j in t:
#             if j not in dic:
#                 return False
#             else:
#                 dic[j] -= 1
#                 if dic[j]==0: del dic[j]
#         return not dic