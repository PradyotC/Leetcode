/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 61.78 %
    Runtime : 77 ms
    Memory Usage : 14.4 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 48.11 % of python3 submissions.
        Your memory usage beats 96.97 % of python3 submissions.
}
*/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def retdict(r):
            rdict = {}
            for i in r:
                if i in rdict:
                    rdict[i]+=1
                else:
                    rdict[i]=1
            return rdict
        
        return retdict(s)==retdict(t)