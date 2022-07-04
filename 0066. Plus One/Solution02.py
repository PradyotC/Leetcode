/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.07 %
    Runtime : 55 ms
    Memory Usage : 13.9 MB
    Testcase : 111 / 111 passed
    Ranking : 
        Your runtime beats 35.39 % of python3 submissions.
        Your memory usage beats 58.17 % of python3 submissions.
}
*/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        i = len(digits)-1
        while i>-1:
            if c!=1: return digits
            temp = digits[i]+c
            digits[i] = temp%10
            c = temp//10
            i-=1
        if c==1: digits.insert(0,c)
        return digits