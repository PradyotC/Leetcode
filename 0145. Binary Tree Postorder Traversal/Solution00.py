/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 64.98 %
    Runtime : 29 ms
    Memory Usage : 13.8 MB
    Testcase : 68 / 68 passed
    Ranking : 
        Your runtime beats 95.92 % of python3 submissions.
        Your memory usage beats 96.39 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]