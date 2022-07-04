/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.24 %
    Runtime : 66 ms
    Memory Usage : 14.3 MB
    Testcase : 43 / 43 passed
    Ranking : 
        Your runtime beats 48.32 % of python3 submissions.
        Your memory usage beats 18.82 % of python3 submissions.
}
*/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sett = {}
        sett1 = {}
        for i in range(len(s)):
            if s[i] not in sett and t[i] not in sett1:
                sett[s[i]]=t[i]
                sett1[t[i]]=s[i]
            elif s[i] in sett and sett[s[i]]!=t[i]: return False
            elif t[i] in sett1 and sett1[t[i]]!=s[i]: return False
        return True