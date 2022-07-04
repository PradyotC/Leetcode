/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.97 %
    Runtime : 2491 ms
    Memory Usage : 18.8 MB
    Testcase : 50 / 50 passed
    Ranking : 
        Your runtime beats 00.00 % of submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for j in range(n)] for i in range (m)]
        bfs = []
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    bfs += [(i,j,0)]
        while bfs:
            a,b,c = bfs.pop(0)
            if a<0 or a>=m or b<0 or b>=n: continue
            if visited[a][b]==1: continue
            visited[a][b]=1
            if mat[a][b]!=0: 
                mat[a][b]=c+1
                c+=1
            bfs.extend([(a,b-1,c),(a,b+1,c),(a-1,b,c),(a+1,b,c)])    
        return mat
            
        
        
        
        
        
        
        
        
        
        
        
    def prmat(self,grid):
        m1,n1 = len(grid),len(grid[0])
        print("",end="\t\t")
        [print(i,end="\t") for i in range(m)]
        print()
        print()
        for i in range(m):
            print(i,end="\t\t")
            for j in range(n):
                print(grid[i][j],end="\t")
            print()
        print()
            