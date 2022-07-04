/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 61.54 %
    Runtime : 56 ms
    Memory Usage : 14.8 MB
    Testcase : 34 / 34 passed
    Ranking : 
        Your runtime beats 42.59 % of python3 submissions.
        Your memory usage beats 19.75 % of python3 submissions.
}
*/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels















# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root: return []
#         if not (root.left or root.right): return [[root.val]]
#         self.level = 0
#         def lvl(r,d):
#             if not r: return
#             self.level = max(self.level,d)
#             lvl(r.left,d+1)
#             lvl(r.right,d+1)
#         lvl(root,0)
#         self.ans = [[root.val]]+[[] for i in range(self.level)]
#         def wrt(r,d):
#             if not r: return
#             if r.left:
#                 self.ans[d]+=[r.left.val]
#                 wrt(r.left,d+1)
#             if r.right:
#                 self.ans[d]+=[r.right.val]
#                 wrt(r.right,d+1)
#         wrt(root,1)
#         return self.ans