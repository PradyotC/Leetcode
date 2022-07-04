/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 75.33 %
    Runtime : 209 ms
    Memory Usage : 18.4 MB
    Testcase : 477 / 477 passed
    Ranking : 
        Your runtime beats 90.27 % of python3 submissions.
        Your memory usage beats 47.04 % of python3 submissions.
}
*/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l1 = len(s)
        if l1==1: return s
        l,r = 0,l1-1
        while l-r<1: 
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
        return s
        # i = 0
        # while i<(l//2):
        #     s[i],s[-(i+1)] = s[-(i+1)],s[i]
        #     i+=1
        # return s