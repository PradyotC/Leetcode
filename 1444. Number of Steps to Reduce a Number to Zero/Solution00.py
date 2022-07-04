/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 85.95 %
    Runtime : 31 ms
    Memory Usage : 13.9 MB
    Testcase : 204 / 204 passed
    Ranking : 
        Your runtime beats 91.99 % of python3 submissions.
        Your memory usage beats 52.21 % of python3 submissions.
}
*/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num in (0,1): return num
        ret = 0
        while num!=0:
            if num%2==0:
                num//=2
                ret+=1
            if num%2!=0:
                num-=1
                ret+=1
        return ret