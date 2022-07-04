/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 63.26 %
    Runtime : 42 ms
    Memory Usage : 13.9 MB
    Testcase : 69 / 69 passed
    Ranking : 
        Your runtime beats 62.79 % of python3 submissions.
        Your memory usage beats 58.72 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)