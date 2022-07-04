/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.32 %
    Runtime : 153 ms
    Memory Usage : 14.4 MB
    Testcase : 20 / 20 passed
    Ranking : 
        Your runtime beats 10.53 % of python3 submissions.
        Your memory usage beats 17.20 % of python3 submissions.
}
*/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def eval(a,b,sym):
            if sym=="+": return a+b
            if sym=="-": return a-b
            if sym=="/": return int(a/b)
            if sym=="*": return a*b
        while tokens:
            char = tokens.pop(0)
            if char in ("+","-","/","*"):
                b = stack.pop()
                a = stack.pop()
                stack.extend([eval(a,b,char)])
            else:
                stack.extend([int(char)])
        return stack[0]