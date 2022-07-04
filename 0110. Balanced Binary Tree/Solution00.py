/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 47.26 %
    Runtime : 66 ms
    Memory Usage : 18.6 MB
    Testcase : 228 / 228 passed
    Ranking : 
        Your runtime beats 73.89 % of python3 submissions.
        Your memory usage beats 61.34 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        if not (root.left or root.right): return True
        def bal(r):
            if not r: return (0,True)
            if not (r.left or r.right): return (1,True)
            hl,bl = bal(r.left)
            hr,br = bal(r.right)
            if bl and br and abs(hl-hr)<2: return (max(hl,hr)+1,True)
            return (max(hl,hr)+1,False)
        return bal(root)[1]
        