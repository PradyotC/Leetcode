/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.66 %
    Runtime : 34 ms
    Memory Usage : 13.9 MB
    Testcase : 25 / 25 passed
    Ranking : 
        Your runtime beats 85.61 % of python3 submissions.
        Your memory usage beats 29.91 % of python3 submissions.
}
*/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []
        self.ans = []
        self.dictt = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        def back(s,ans):
            if not s: 
                self.ans.append(ans)
                return
            k = self.dictt[s[0]]
            s = s[1:]
            for i in k:
                back(str(s),ans+i)
        back(str(digits),"")
        return self.ans
        