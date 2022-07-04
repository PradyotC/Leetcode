/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 30.81 %
    Runtime : 56 ms
    Memory Usage : 16.3 MB
    Testcase : 80 / 80 passed
    Ranking : 
        Your runtime beats 72.99 % of python3 submissions.
        Your memory usage beats 91.61 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        m = pow(-2,31)-1
        current = root
        stack = []
        #using stack for inorder traversal
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                if m>=current.val: return False
                m = current.val
                current = current.right
            else:
                break
        return True