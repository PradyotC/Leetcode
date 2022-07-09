class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.reslen = 0
        def pal(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>self.reslen:
                    self.reslen = r-l+1
                    self.start = l
                l -= 1
                r += 1
        for i in range(len(s)):
            pal(i,i)    #for checking odd palindrome
            pal(i,i+1)  #for checking even palindrome
        return s[self.start:self.start+self.reslen]