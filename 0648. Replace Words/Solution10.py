/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 62.35 %
    Runtime : 206 ms
    Memory Usage : 36.2 MB
    Testcase : 126 / 126 passed
    Ranking : 
        Your runtime beats 52.34 % of python3 submissions.
        Your memory usage beats 19.03 % of python3 submissions.
}
*/

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
        cur.end = True
    
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
        while dictionary:
            trie.insert(dictionary.pop())
        sentence = sentence.split()
        ret = ""
        while sentence:
            ret+=trie.replace(sentence.pop(0))
        return ret.rstrip()