/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 58.26 %
    Runtime : 26 ms
    Memory Usage : 13.8 MB
    Testcase : 34 / 34 passed
    Ranking : 
        Your runtime beats 98.61 % of python3 submissions.
        Your memory usage beats 61.04 % of python3 submissions.
}
*/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [[1],[1,1]]
        if rowIndex in (0,1): return ret[rowIndex]
        prev = [1,1]
        k = 2
        while k<=rowIndex:
            j = k-1
            curr = [1]+[0 for i in range(j)]+[1]
            for i in range(1,k):
                curr[i] = prev[i-1]+prev[i]
            k+=1
            prev = curr
        return curr
        