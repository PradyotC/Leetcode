/*
Submission Detail:{
    Difficulty : Hard
    Acceptance Rate : 55.76 %
    Runtime : 1303 ms
    Memory Usage : 14.3 MB
    Testcase : 100 / 100 passed
    Ranking : 
        Your memory usage beats 76.65 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0,0)
        cuts.append(n)
        l = len(cuts)
        opt = [[ inf for i in range(l) ] for i in range(l)]
        for i in range(l,-1,-1):
            for j in range(i,l):
                if j == i+1:
                    opt[i][j] = 0
                else:
                    for k in range(i,j):
                        opt[i][j] = min(opt[i][j], (cuts[j]-cuts[i]) + opt[i][k]+opt[k][j])
        return opt[0][l-1]