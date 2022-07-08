class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.reslen = 0
        def pal(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>self.reslen:
                    self.reslen = r-l+1
                    self.res = s[l:r+1]
                l -= 1
                r += 1
        for i in range(len(s)):
            pal(i,i)    #for checking odd palindrome
            pal(i,i+1)  #for checking even palindrome
        return self.res