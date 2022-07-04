/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.14 %
    Runtime : 281 ms
    Memory Usage : 31.4 MB
    Testcase : 16 / 16 passed
    Ranking : 
        Your runtime beats 44.88 % of python3 submissions.
        Your memory usage beats 72.22 % of python3 submissions.
}
*/

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: return False
            cur = cur.children[c]
        return cur.endOfWord
    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)