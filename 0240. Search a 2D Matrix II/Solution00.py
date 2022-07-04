/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.89 %
    Runtime : 172 ms
    Memory Usage : 20.3 MB
    Testcase : 129 / 129 passed
    Ranking : 
        Your runtime beats 96.73 % of python3 submissions.
        Your memory usage beats 84.49 % of python3 submissions.
}
*/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        N,M = len(matrix), len(matrix[0])
        r,c = N-1,0
        while r >= 0 and c < M:
            if matrix[r][c]== target: return True
            if matrix[r][c] < target: c+=1
            else: r-=1
        return False