/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 44.86 %
    Runtime : 32 ms
    Memory Usage : 14 MB
    Testcase : 45 / 45 passed
    Ranking : 
        Your runtime beats 98.87 % of python3 submissions.
        Your memory usage beats 45.06 % of python3 submissions.
}
*/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = wordDict
        opt = [False] * (len(s))
        opt.append(True)
        for i in range(len(s)-1,-1,-1):
            for j in wordDict:
                if (i + len(j)) <= len(s) and s[i:i+len(j)] == j:
                    opt[i] = opt[i+len(j)]
                if opt[i]:
                    break
        return opt[0]