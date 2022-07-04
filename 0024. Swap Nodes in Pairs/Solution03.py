/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.30 %
    Runtime : 30 ms
    Memory Usage : 14 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 95.62 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        h1 = head
        def sp(h):
            if not h: return
            if not h.next: return h
            h2 = sp(h.next.next)
            h.next.next = h
            h = h.next
            h.next.next = h2
            return h
        return sp(h1)