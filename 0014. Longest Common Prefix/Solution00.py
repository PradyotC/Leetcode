/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 39.88 %
    Runtime : 48 ms
    Memory Usage : 14 MB
    Testcase : 123 / 123 passed
    Ranking : 
        Your runtime beats 62.76 % of python3 submissions.
        Your memory usage beats 49.69 % of python3 submissions.
}
*/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs = sorted(strs)
        str1 = strs[0]
        str2 = strs[-1]
        ans = ""
        for i in range(min(len(str1),len(str2))):
            if str1[i]!=str2[i]:
                return ans
            ans+=str1[i]
        return ans