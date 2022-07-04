/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 70.72 %
    Runtime : 58 ms
    Memory Usage : 14.1 MB
    Testcase : 8 / 8 passed
    Ranking : 
        Your runtime beats 40.82 % of python3 submissions.
        Your memory usage beats 76.81 % of python3 submissions.
}
*/

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