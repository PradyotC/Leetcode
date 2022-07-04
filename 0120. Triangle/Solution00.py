/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.91 %
    Runtime : 153 ms
    Memory Usage : 14.9 MB
    Testcase : 44 / 44 passed
    Ranking : 
        Your runtime beats 8.07 % of python3 submissions.
        Your memory usage beats 92.34 % of python3 submissions.
}
*/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n==0: return 0
        if n==1: return triangle[0][0]
        opt = [triangle[0],[]]
        for i in range(1,n):
            for j in range(i):
                if j==0: opt[1].append(triangle[i][0]+opt[0][0])
                else:
                    opt[1].append(triangle[i][j]+min(opt[0][j-1],opt[0][j]))
            opt[1].append(triangle[i][i]+opt[0][i-1])
            opt.pop(0)
            opt.append([])
        return min(opt[0])
        