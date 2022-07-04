/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 53.63 %
    Runtime : 58 ms
    Memory Usage : 13.9 MB
    Testcase : 404 / 404 passed
    Ranking : 
        Your runtime beats 37.29 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         self.sqr = {i:i*i for i in range(10)}
        
#         def rec(num):
#             if num==1: return True
#             ans = 0
#             while n!=0:
#                 ans+=self.sqr[num%10]
#                 num//=10
#             return rec(ans)
        
#         try:
#             return rec(n)
#         except:
#             return False

class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1: return True
        sett = set([n])
        ans = n
        while ans!=1:
            n = ans
            ans = 0
            while n!=0:
                x = n%10
                ans+=x*x
                n//=10
            if ans in sett: return False
            sett.add(ans)
        return True