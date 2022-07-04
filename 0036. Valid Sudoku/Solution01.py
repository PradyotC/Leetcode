/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 55.70 %
    Runtime : 114 ms
    Memory Usage : 13.9 MB
    Testcase : 507 / 507 passed
    Ranking : 
        Your runtime beats 75.64 % of python3 submissions.
        Your memory usage beats 82.13 % of python3 submissions.
}
*/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictt = {}
        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".": continue
                if board[i][j] in rows[i]: return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]: return False
                cols[j].add(board[i][j])
                m,n = (i//3)*3,(j//3)*3
                if (m,n) in dictt and board[i][j] in dictt[(m,n)]: return False
                if (m,n) not in dictt: dictt[(m,n)]=set({board[i][j]})
                else: dictt[(m,n)].add(board[i][j])
        return True