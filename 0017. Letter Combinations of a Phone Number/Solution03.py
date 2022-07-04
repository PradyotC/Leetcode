/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.66 %
    Runtime : 57 ms
    Memory Usage : 14 MB
    Testcase : 25 / 25 passed
    Ranking : 
        Your runtime beats 19.73 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="": return []
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
        
        def ret(s):
            if s.__len__()==1: return self.dictt[s]
            ans = self.dictt[s[0]]
            a1 = ret(s[1:])
            r1 = []
            for i in ans:
                for j in a1:
                    r1 += [i+j]
            return r1
            
        return ret(digits)