/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.45 %
    Runtime : 2199 ms
    Memory Usage : 35.1 MB
    Testcase : 42 / 42 passed
    Ranking : 
        Your memory usage beats 77.29 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findMaximumXOR(self, nums):
        mask,output = 0,0
        for i in range(32,-1,-1):
            mask = mask | 1<<i
            found = set([n & mask for n in nums])
            temp = output | 1 << i
            for f in found:
                if f^temp in found:
                    output = temp
        return output