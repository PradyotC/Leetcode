/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 36.47 %
    Runtime : 56 ms
    Memory Usage : 13.8 MB
    Testcase : 75 / 75 passed
    Ranking : 
        Your runtime beats 24.66 % of python3 submissions.
        Your memory usage beats 63.36 % of python3 submissions.
}
*/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle=="": return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1