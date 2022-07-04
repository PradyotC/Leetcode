/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 59.30 %
    Runtime : 25 ms
    Memory Usage : 13.9 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your runtime beats 99.17 % of python3 submissions.
        Your memory usage beats 63.57 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head: return
#         if not head.next: return head
#         h1 = head
#         def sp(h):
#             if not h: return
#             if not h.next: return h
#             h2 = sp(h.next.next)
#             h.next.next = h
#             h = h.next
#             h.next.next = h2
#             return h
#         return sp(h1)
    

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        h1 = head
        head = ListNode(-1,head)
        h0 = head
        while h1:
            h2 = h1.next
            if not h2: break
            h1.next = h2.next
            h2.next = h1
            h0.next = h2
            h0 = h1
            h1 = h1.next
        return head.next