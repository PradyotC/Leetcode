/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.48 %
    Runtime : 65 ms
    Memory Usage : 16.2 MB
    Testcase : 38 / 38 passed
    Ranking : 
        Your runtime beats 68.35 % of python3 submissions.
        Your memory usage beats 50.09 % of python3 submissions.
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        if not root.children: return [root.val]
        ret = []
        for i in root.children:
            ret+=self.postorder(i)
        return ret+[root.val]