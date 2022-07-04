/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.78 %
    Runtime : 89 ms
    Memory Usage : 14.5 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 31.13 % of python3 submissions.
        Your memory usage beats 66.63 % of python3 submissions.
}
*/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         def retdict(r):
#             rdict = {}
#             for i in r:
#                 if i in rdict:
#                     rdict[i]+=1
#                 else:
#                     rdict[i]=1
#             return rdict
        
#         return retdict(s)==retdict(t)

        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
                if dic[j]==0: del dic[j]
        return not dic