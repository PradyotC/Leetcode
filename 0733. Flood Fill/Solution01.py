/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 58.83 %
    Runtime : 93 ms
    Memory Usage : 14.5 MB
    Testcase : 277 / 277 passed
    Ranking : 
        Your runtime beats 71.67 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def prmat(gr):
            print()
            for i in gr:
                for j in i:
                    print(j,end="\t")
                print()
                
        n = len(image[0])+2
        image = [[-1]+i+[-1] for i in image]
        image.insert(0,[-1 for i in range(n)])
        image.append([-1 for i in range(n)])
        m = len(image)
        
        sr+=1
        sc+=1
        
        visited = [[-1]+[0 for j in range(n-2)]+[-1] for i in range(m-2)]
        visited.insert(0,[-1 for i in range(n)])
        visited.append([-1 for i in range(n)])
        
        cc1 = image[sr][sc]
        
        def floodfill(i,j,nc,cc):
            if visited[i][j] in (1,-1): return
            visited[i][j]=1
            if image[i][j]==cc:
                image[i][j]=nc
                floodfill(i-1,j,nc,cc)
                floodfill(i,j-1,nc,cc)
                floodfill(i+1,j,nc,cc)
                floodfill(i,j+1,nc,cc)
        
        floodfill(sr,sc,newColor,cc1)
        
        # prmat(image)
        # prmat(visited)
        
        return [i[1:-1] for i in image][1:-1]
        