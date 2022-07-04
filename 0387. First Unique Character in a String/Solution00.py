/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.48 %
    Runtime : 255 ms
    Memory Usage : 14.2 MB
    Testcase : 105 / 105 passed
    Ranking : 
        Your runtime beats 23.74 % of python3 submissions.
        Your memory usage beats 58.74 % of python3 submissions.
}
*/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for index,char in enumerate(s):
            if freq[char] == 1:
                return index
        return -1