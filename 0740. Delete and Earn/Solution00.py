/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 57.49 %
    Runtime : 79 ms
    Memory Usage : 15.9 MB
    Testcase : 49 / 49 passed
    Ranking : 
        Your runtime beats 99.36 % of python3 submissions.
        Your memory usage beats 77.09 % of python3 submissions.
}
*/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        c = {}
        for i in nums:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        ck = list(sorted(c.keys()))
        l = len(ck)
        opt = [ck[0]*c[ck[0]],0]
        if l>1:
            if ck[0]<ck[1]-1:
                opt[1] = opt[0]+ck[1]*c[ck[1]]
            else:
                opt[1] = max(opt[0],ck[1]*c[ck[1]])
            for i in range(2,l):
                if ck[i-1]<ck[i]-1:
                    opt.pop(0)
                    opt.append(opt[0]+ck[i]*c[ck[i]])
                else:
                    opt.append(max(opt.pop(0)+ck[i]*c[ck[i]],opt[0]))
            return opt[-1]
        return opt[0]