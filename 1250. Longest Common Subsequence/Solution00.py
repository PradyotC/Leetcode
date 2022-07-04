/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 58.97 %
    Runtime : 588 ms
    Memory Usage : 22.6 MB
    Testcase : 44 / 44 passed
    Ranking : 
        Your runtime beats 60.38 % of python3 submissions.
        Your memory usage beats 56.74 % of python3 submissions.
}
*/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        opt = [[0 for i in range(len(text2)+1)]]
        for i in range(1,len(text1)+1):
            opt.append([0 for i in range(len(text2)+1)])
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    b1 = 1
                else:
                    b1 = 0
                # print(i,j,"\t",i-1,j,"\t",i,j-1,"\t",i-1,j-1)
                opt[i][j] = max(opt[i-1][j],opt[i][j-1],opt[i-1][j-1]+b1)
        return opt[i][j]
                
                