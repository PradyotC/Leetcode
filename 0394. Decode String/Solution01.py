/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.67 %
    Runtime : 44 ms
    Memory Usage : 13.9 MB
    Testcase : 34 / 34 passed
    Ranking : 
        Your runtime beats 54.13 % of python3 submissions.
        Your memory usage beats 71.18 % of python3 submissions.
}
*/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i=="]":
                str1=""
                k = stack.pop()
                while k!="[":
                    str1 = k+str1
                    k = stack.pop()
                stack.append(str1*int(stack.pop()))
            elif i.isnumeric():
                if stack and stack[-1].isnumeric(): stack[-1]+=i
                else: stack.append(i)
            else: stack.append(i)
        return ''.join(stack)