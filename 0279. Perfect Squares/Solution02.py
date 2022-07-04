/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.04 %
    Runtime : 5691 ms
    Memory Usage : 15.2 MB
    Testcase : 588 / 588 passed
    Ranking : 
        Your runtime beats 34.51 % of python3 submissions.
        Your memory usage beats 23.77 % of python3 submissions.
}
*/

class Solution:
    def numSquares(self, n: int) -> int:
        if n==1: return 1
        sq = [i*i for i in range(int(math.sqrt(n)),1,-1)]
        count = float('inf')
        queue = [(n,0)]
        visited = {}
        while queue:
            n1,c1 = queue.pop(0)
            if n1==0:
                count = min(count,c1)
                visited[0] = count
                continue
            if n1<4:
                count = min(count,c1+n1)
                visited[0] = count
                continue
            ret = []
            for i in sq:
                if i<=n1:
                    if n1-i not in visited or visited[n1-i]>c1+1:
                        visited[n1-i] = c1+1
                        ret.append((n1-i,c1+1))
            queue.extend(ret)
        return count
            
            
            
            