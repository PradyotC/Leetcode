/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 43.79 %
    Runtime : 17345 ms
    Memory Usage : 78.1 MB
    Testcase : 29 / 29 passed
    Ranking : 
        Your runtime beats 25.64 % of python3 submissions.
        Your memory usage beats 29.44 % of python3 submissions.
}
*/

class TrieNode():
    def __init__(self):
        self.child = {}
        self.end = False
        
class WordDictionary:

    def __init__(self): self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child: cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.end = True
        
    def search(self, word: str) -> bool:
        def dfs(j,cur):
            for i in range(j,len(word)):
                c = word[i]
                if c==".":
                    for child in cur.child.values():
                        if dfs(i+1,child): return True
                    return False
                else:
                    if c not in cur.child: return False
                    cur = cur.child[c]
            return cur.end
        return dfs(0,self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)