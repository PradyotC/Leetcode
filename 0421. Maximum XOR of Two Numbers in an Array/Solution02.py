/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 54.45 %
    Runtime : 4899 ms
    Memory Usage : 146.3 MB
    Testcase : 42 / 42 passed
    Ranking : 
        Your memory usage beats 6.00 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        
    def search(self,word):
        cur = self.root
        ret = ''
        for c in word:
            if c in cur.children: 
                cur = cur.children[c]
                ret+=c
            else:
                if c=='0': 
                    cur = cur.children['1']
                    ret+='1'
                else: 
                    cur = cur.children['0']
                    ret+='0'
        return int(ret,2)

class Solution:
    def con2bin(self,n,l):
        if n: ret = ('0'*(l - n.bit_length()))
        else: ret = ('0'*(l - n.bit_length() - 1))
        return ret+format(n, "b")
    
    def invert(self,n):
        ret = ''
        for i in n:
            if i=='0': ret+='1'
            else: ret+='0'
        return ret
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        l1 = max(nums).bit_length()
        binn = []
        for i in nums:
            binn.append(self.con2bin(i,l1))
        tri = Trie()
        for i in binn:
            # print(i)
            tri.insert(i)
        m = 0
        for i,j in zip(binn,nums):
            ans = tri.search(self.invert(i)) ^ j
            m = max(m,ans)
        return m