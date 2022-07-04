/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 75.33 %
    Runtime : 232 ms
    Memory Usage : 18.5 MB
    Testcase : 477 / 477 passed
    Ranking : 
        Your runtime beats 73.97 % of python3 submissions.
        Your memory usage beats 47.04 % of python3 submissions.
}
*/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l==1: return s
        i = 0
        while i<(l//2):
            s[i],s[-(i+1)] = s[-(i+1)],s[i]
            i+=1
        return s