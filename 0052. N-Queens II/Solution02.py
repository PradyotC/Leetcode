/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 69.95 %
    Runtime : 46 ms
    Memory Usage : 13.9 MB
    Testcase : 9 / 9 passed
    Ranking : 
        Your runtime beats 94.26 % of python3 submissions.
        Your memory usage beats 37.29 % of python3 submissions.
}
*/

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==1: return 1
        if n in (0,2,3): return 0
        self.count = 0
        self.summ = set()
        self.diff = set()
        self.visited = [None for i in range(n)]
        def nqueen(i):
            if i==n:
                self.count+=1
                return
            for k in range(n):
                if self.visited[k]: continue
                if k+i in self.summ: continue
                if k-i in self.diff: continue
                # print(i,k)
                self.visited[k]=1
                self.summ.add(k+i)
                self.diff.add(k-i)
                nqueen(i+1)
                self.summ.remove(k+i)
                self.diff.remove(k-i)
                self.visited[k]=None
        for i in range(n):
            self.visited[i]=1
            self.summ.add(i+0)
            self.diff.add(i-0)
            nqueen(1)
            self.visited[i]=None
            self.summ.remove(i+0)
            self.diff.remove(i-0)
        return self.count
            