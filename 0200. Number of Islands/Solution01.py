/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.58 %
    Runtime : 693 ms
    Memory Usage : 16.2 MB
    Testcase : 49 / 49 passed
    Ranking : 
        Your runtime beats 10.13 % of python3 submissions.
        Your memory usage beats 97.35 % of python3 submissions.
}
*/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        island = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and int(grid[i][j])==1:
                    stack = [(i,j)]
                    while stack:
                        a,b = stack.pop()
                        if a<0 or a>=m or b<0 or b>=n: continue
                        if visited[a][b]==1: continue
                        if int(grid[a][b])==0: continue
                        visited[a][b]=1
                        stack.extend([(a,b+1),(a,b-1),(a+1,b),(a-1,b)])
                    island += 1
        return island