/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 71.37 %
    Runtime : 34 ms
    Memory Usage : 13.8 MB
    Testcase : 70 / 70 passed
    Ranking : 
        Your runtime beats 86.21 % of python3 submissions.
        Your memory usage beats 59.30 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)