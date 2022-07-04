/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.93 %
    Runtime : 138 ms
    Memory Usage : 14.8 MB
    Testcase : 164 / 164 passed
    Ranking : 
        Your runtime beats 87.12 % of python3 submissions.
        Your memory usage beats 52.67 % of python3 submissions.
}
*/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        row,col = set(),set()
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(n): matrix[i][j] = 0
        for i in col:
            for j in range(m): matrix[j][i] = 0