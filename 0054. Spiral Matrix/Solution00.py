/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 42.17 %
    Runtime : 31 ms
    Memory Usage : 13.9 MB
    Testcase : 23 / 23 passed
    Ranking : 
        Your runtime beats 92.89 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix),len(matrix[0])
        row,col=set(),set()
        i,j=0,0
        step = 0
        ret = []
        while i not in row or j not in col:
            s = step%4
            if s==0:
                row.add(i)
                for k in range(n):
                    if k in col: continue
                    ret.append(matrix[i][k])
                    j = k
            if s==1:
                col.add(j)
                for k in range(m):
                    if k in row: continue
                    ret.append(matrix[k][j])
                    i = k
            if s==2:
                row.add(i)
                for k in range(n-1,-1,-1):
                    if k in col: continue
                    ret.append(matrix[i][k])
                    j = k
            if s==3:
                col.add(j)
                for k in range(m-1,-1,-1):
                    if k in row: continue
                    ret.append(matrix[k][j])
                    i = k
            step+=1
        return ret
            