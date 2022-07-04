/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.06 %
    Runtime : 136 ms
    Memory Usage : 26.4 MB
    Testcase : 31 / 31 passed
    Ranking : 
        Your runtime beats 22.23 % of python3 submissions.
        Your memory usage beats 30.52 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def lca(r,p1,q1):
            if not r: return False
            if not (r.left or r.right):
                if r==p1 or r==q1: return True
                return False
            b1 = lca(r.left,p1,q1)
            b2 = lca(r.right,p1,q1)
            # print(b1,b2,r.val,self.ans)
            if (r==p1 or r==q1):
                if b1 or b2: self.ans = r
                return True
            if b1 and b2: 
                self.ans = r
                return True
            if b1 or b2: return True
            return False
        lca(root,p,q)
        return self.ans