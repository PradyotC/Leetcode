/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 77.74 %
    Runtime : 51 ms
    Memory Usage : 13.9 MB
    Testcase : 112 / 112 passed
    Ranking : 
        Your runtime beats 34.66 % of python3 submissions.
        Your memory usage beats 65.10 % of python3 submissions.
}
*/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if str=="": return ""
        for i in range(len(word)):
            if word[i]==ch:
                if i!=len(word)-1:
                    return word[:i+1][::-1]+word[i+1:]
                else:
                    return word[::-1]
        return word
        
                