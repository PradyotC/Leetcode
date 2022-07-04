/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.66 %
    Runtime : 36 ms
    Memory Usage : 13.8 MB
    Testcase : 25 / 25 passed
    Ranking : 
        Your runtime beats 79.25 % of python3 submissions.
        Your memory usage beats 78.08 % of python3 submissions.
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
            return [i+j for i in self.dictt[s[0]] for j in ret(s[1:])]
            
        return ret(digits)