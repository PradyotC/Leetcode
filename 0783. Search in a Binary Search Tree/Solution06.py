/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 76.68 %
    Runtime : 140 ms
    Memory Usage : 16.5 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 20.99 % of python3 submissions.
        Your memory usage beats 69.46 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return
        if root.val==val: return root
        self.val = val
        self.ans = None
        def search(r):
            if not r: return False
            if r.val==self.val: 
                self.ans = r
                return True
            if r.val>self.val and search(r.left): return True
            if r.val<self.val and search(r.right): return True
            return False
        search(root)
        return self.ans
            
            
            