/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.79 %
    Runtime : 60 ms
    Memory Usage : 14.2 MB
    Testcase : 22 / 22 passed
    Ranking : 
        Your runtime beats 44.76 % of python3 submissions.
        Your memory usage beats 98.08 % of python3 submissions.
}
*/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        if not node.neighbors: return Node(node.val)
        ret = Node(node.val)
        self.stack={node:ret}
        self.travel=set({node})
        def clone(r,n):
            r.neighbors = []
            for i in n.neighbors:
                if i not in self.stack:
                    self.stack[i]=Node(i.val)
                r.neighbors.append(self.stack[i])
            for i in n.neighbors:
                if i not in self.travel:
                    self.travel.add(i)
                    clone(self.stack[i],i)
        clone(ret,node)
        return ret
        
                    