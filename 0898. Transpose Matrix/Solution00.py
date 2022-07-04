/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.89 %
    Runtime : 112 ms
    Memory Usage : 14.7 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 48.98 % of python3 submissions.
        Your memory usage beats 57.15 % of python3 submissions.
}
*/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ret = [[] for i in range(n)]
        for i in range(m):
            for j in range(n):
                ret[j].append(matrix[i][j])
        return ret
                