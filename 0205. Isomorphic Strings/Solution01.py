/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 42.24 %
    Runtime : 65 ms
    Memory Usage : 14.1 MB
    Testcase : 43 / 43 passed
    Ranking : 
        Your runtime beats 50.18 % of python3 submissions.
        Your memory usage beats 89.00 % of python3 submissions.
}
*/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sett = {}
        sett1 = {}
        for i in range(len(s)):
            # print(s[i],t[i])
            if s[i] not in sett and t[i] not in sett1:
                sett[s[i]]=t[i]
                sett1[t[i]]=s[i]
                # s = s.replace(s[i],t[i])
                # print(sett,sett1)
                # print(s[i] in sett and sett[s[i]]!=t[i])
            elif s[i] in sett and sett[s[i]]!=t[i]: return False
            elif t[i] in sett1 and sett1[t[i]]!=s[i]: return False
        return True