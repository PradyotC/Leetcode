/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.07 %
    Runtime : 261 ms
    Memory Usage : 88.7 MB
    Testcase : 202 / 202 passed
    Ranking : 
        Your runtime beats 32.96 % of python3 submissions.
        Your memory usage beats 34.37 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder==[]: return None
        if len(inorder)==1: return TreeNode(inorder[0])
        idx = inorder.index(postorder[-1])
        if idx == 0: return TreeNode(postorder[-1],None,self.buildTree(inorder[1:],postorder[:-1]))
        if idx == len(inorder)-1: return TreeNode(postorder[-1],self.buildTree(inorder[:-1],postorder[:-1]),None)
        linorder,rinorder = inorder[:idx],inorder[idx+1:]
        lpsorder,rpsorder = postorder[:-(len(rinorder)+1)],postorder[-(len(rinorder)+1):-1]
        return TreeNode(postorder[-1],self.buildTree(linorder,lpsorder),self.buildTree(rinorder,rpsorder))