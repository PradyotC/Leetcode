/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 55.01 %
    Runtime : 1511 ms
    Memory Usage : 13.9 MB
    Testcase : 6 / 6 passed
    Ranking : 
        Your runtime beats 5.14 % of python3 submissions.
        Your memory usage beats 96.28 % of python3 submissions.
}
*/

class Solution:
    
    def valid(self,r,c,k):
        if any(self.brd[r][i]==k for i in range(9)): return False
        if any(self.brd[i][c]==k for i in range(9)): return False
        r,c = (r//3)*3,c//3*3
        if any(self.brd[i][j]==k for i in range(r,r+3) for j in range(c,c+3)): return False
        return True
    
    def backtrack(self,r,c):
        while self.brd[r][c]!='.':
            c+=1
            r+=c//9
            c%=9
            if r==9: return True
        for i in range(1,10):
            k = str(i)
            if self.valid(r,c,k):
                self.brd[r][c]=k
                if self.backtrack(r,c): return True
        self.brd[r][c]='.'
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.brd = board
        self.backtrack(0,0)