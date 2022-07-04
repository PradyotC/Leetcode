/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 49.35 %
    Runtime : 94 ms
    Memory Usage : 14 MB
    Testcase : 166 / 166 passed
    Ranking : 
        Your runtime beats 6.98 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        h1 = head
        nhead = head.next
        while nhead:
            if head.val == nhead.val:
                head.next = nhead.next
            else:
                head = head.next
            if nhead.next:
                nhead = nhead.next
            else:
                break
        return h1