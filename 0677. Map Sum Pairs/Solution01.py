/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.97 %
    Runtime : 55 ms
    Memory Usage : 14.1 MB
    Testcase : 35 / 35 passed
    Ranking : 
        Your runtime beats 35.19 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.val = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix: 
            if c not in cur.children: return 0
            cur = cur.children[c]
        ret = cur.val
        if cur.children:
            stack = list(cur.children.values())
            while stack:
                # print(stack)
                tnode = stack.pop()
                # print(tnode.val)
                ret+=tnode.val
                stack+=tnode.children.values()
        return ret


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)