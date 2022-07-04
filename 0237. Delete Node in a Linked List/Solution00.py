/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 72.66 %
    Runtime : 58 ms
    Memory Usage : 14.3 MB
    Testcase : 41 / 41 passed
    Ranking : 
        Your runtime beats 52.46 % of python3 submissions.
        Your memory usage beats 52.22 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next