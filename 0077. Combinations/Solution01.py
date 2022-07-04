/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 64.77 %
    Runtime : 451 ms
    Memory Usage : 15.9 MB
    Testcase : 27 / 27 passed
    Ranking : 
        Your runtime beats 66.33 % of python3 submissions.
        Your memory usage beats 50.99 % of python3 submissions.
}
*/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l1 = [[i] for i in range(1,n+1)]
        if k==1: return l1
        self.ans = []
        def com(h,lst):
            if h==k: 
                self.ans.append(lst.copy())
                return
            for i in range(lst[-1]+1,n+1):
                lst.append(i)
                com(h+1,lst)
                lst.pop()    
        for i in range(n):
            com(1,l1[i])
        return self.ans
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []
#         q = [(1,[i]) for i in range(1,n+1)]
#         while q:
#             a,b = q.pop(0)
#             if a==k:
#                 ans.append(b)
#                 continue
#             for i in range(b[-1]+1,n+1):
#                 q.append((a+1,b+[i]))
#         return ans