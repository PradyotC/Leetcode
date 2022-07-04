/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 33.47 %
    Runtime : 236 ms
    Memory Usage : 14 MB
    Testcase : 987 / 987 passed
    Ranking : 
        Your runtime beats 18.90 % of python3 submissions.
        Your memory usage beats 49.40 % of python3 submissions.
}
*/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(i,j): return len(s[i:j+1])!=len(set(s[i:j+1]))
        dictt = {}
        left = 0
        right = 0
        length = 0
        while right<len(s):
            if check(left,right): left = dictt[s[right]]+1
            dictt[s[right]]=right
            length = max(length,right-left+1)
            right+=1
        return length
            
        