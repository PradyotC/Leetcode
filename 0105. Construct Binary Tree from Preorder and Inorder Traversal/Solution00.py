/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 58.44 %
    Runtime : 262 ms
    Memory Usage : 88.7 MB
    Testcase : 203 / 203 passed
    Ranking : 
        Your runtime beats 39.22 % of python3 submissions.
        Your memory usage beats 17.75 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder==[]: return None
        if len(inorder)==1: return TreeNode(inorder[0])
        idx = inorder.index(preorder[0])
        if idx == 0: return TreeNode(preorder[0],None,self.buildTree(preorder[1:],inorder[1:]))
        if idx == len(inorder)-1: return TreeNode(preorder[0],self.buildTree(preorder[1:],inorder[:-1]),None)
        linorder,rinorder = inorder[:idx],inorder[idx+1:]
        lprorder,rprorder = preorder[1:1+len(linorder)],preorder[1+len(linorder):]
        return TreeNode(preorder[0],self.buildTree(lprorder,linorder),self.buildTree(rprorder,rinorder))