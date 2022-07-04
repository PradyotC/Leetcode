/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 57.87 %
    Runtime : 131 ms
    Memory Usage : 18.7 MB
    Testcase : 27 / 27 passed
    Ranking : 
        Your runtime beats 36.98 % of python3 submissions.
        Your memory usage beats 68.46 % of python3 submissions.
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
        if not root: return None
        if root.val<=p.val and root.val>=q.val: return root
        if root.val>=p.val and root.val<=q.val: return root
        if root.val<p.val and root.val<q.val: return self.lowestCommonAncestor(root.right,p,q)
        if root.val>p.val and root.val>q.val: return self.lowestCommonAncestor(root.left,p,q)
        