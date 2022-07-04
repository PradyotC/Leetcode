/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 62.35 %
    Runtime : 262 ms
    Memory Usage : 42.6 MB
    Testcase : 126 / 126 passed
    Ranking : 
        Your runtime beats 38.92 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

''' Using Trie'''

class TrieNode:
    def __init__(self):
        self.childs = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.childs: cur.childs[c] = TrieNode()
            cur = cur.childs[c]
            if cur.end: return
        cur.end = True
        if cur.childs: 
            del cur.childs
            cur.childs={}
    
    def replace(self,word):
        cur = self.root
        ret = ""
        for c in word:
            if c not in cur.childs: return word+" "
            ret+=c
            cur = cur.childs[c]
            if cur.end: break
        return ret+" "
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        while dictionary: trie.insert(dictionary.pop())
        ret = ""
        sentence = sentence.split()
        while sentence: ret+=trie.replace(sentence.pop(0))
        return ret.rstrip()


# '''Using Set (Prefix Set)'''
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         prefix = set()
#         while dictionary:
#             s = dictionary.pop()
#             ret = ""
#             while s:
#                 ret+=s.pop(0)
#                 if ret in prefix: break
#             prefix.add(ret)
            
            