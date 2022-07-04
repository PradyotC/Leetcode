/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.88 %
    Runtime : 73 ms
    Memory Usage : 13.9 MB
    Testcase : 3999 / 3999 passed
    Ranking : 
        Your runtime beats 52.21 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def romanToInt(self, s: str) -> int:
        dictt = {"I":1,
                 "V":5,
                 "X":10,
                 "L":50,
                 "C":100,
                 "D":500,
                 "M":1000}
        sum1 = dictt[s[-1]]
        s = s[::-1]
        for i in range(1,len(s)):
            if dictt[s[i-1]]>dictt[s[i]]:
                sum1-=dictt[s[i]]
            else:
                sum1+=dictt[s[i]]
        return sum1