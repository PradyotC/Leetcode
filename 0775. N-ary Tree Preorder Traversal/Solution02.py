/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.37 %
    Runtime : 51 ms
    Memory Usage : 16.2 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 94.93 % of python3 submissions.
        Your memory usage beats 48.59 % of python3 submissions.
}
*/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        if not root.children: return [root.val]
        ret = [root.val]
        for i in root.children:
            ret+=self.preorder(i)
        return ret
        
        