/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 40.85 %
    Runtime : 52 ms
    Memory Usage : 14 MB
    Testcase : 91 / 91 passed
    Ranking : 
        Your runtime beats 38.36 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False
        if s=="": return True
        stk = []
        for i in s:
            if i in ("(","{","["):
                stk.insert(0,i)
            elif i in (")","}","]") and len(stk)==0: return False
            elif i==")":
                if stk[0]=="(":
                    stk.pop(0)
                else:
                    return False
            elif i=="]":
                if stk[0]=="[":
                    stk.pop(0)
                else:
                    return False
            elif i=="}":
                if stk[0]=="{":
                    stk.pop(0)
                else:
                    return False
        if len(stk) == 0: return True
        return False