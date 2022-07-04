/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.48 %
    Runtime : 275 ms
    Memory Usage : 14.3 MB
    Testcase : 105 / 105 passed
    Ranking : 
        Your runtime beats 20.62 % of python3 submissions.
        Your memory usage beats 18.12 % of python3 submissions.
}
*/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = {}
        for i in range(s.__len__()):
            if s[i] in ans: 
                ans[s[i]]=s.__len__()
            else:
                ans[s[i]]=i
        m = min(ans.values())
        if m==s.__len__(): return -1
        return m
        