/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 70.72 %
    Runtime : 59 ms
    Memory Usage : 14.3 MB
    Testcase : 8 / 8 passed
    Ranking : 
        Your runtime beats 38.45 % of python3 submissions.
        Your memory usage beats 39.77 % of python3 submissions.
}
*/

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def par(s,op,cl):
            if cl==n: 
                self.ans.append(s)
                return
            if op!=n: par(s+'(',op+1,cl)
            if cl<op: par(s+')',op,cl+1)
        par('',0,0)
        return self.ans
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack (openN, closedN) :
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN != n:
                stack.append("(")
                backtrack(openN+ 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
        
        
        
        
        
        
        
        
        
        
        
    
    