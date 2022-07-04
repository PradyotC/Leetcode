/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 43.95 %
    Runtime : 73 ms
    Memory Usage : 17.8 MB
    Testcase : 66 / 66 passed
    Ranking : 
        Your runtime beats 90.16 % of python3 submissions.
        Your memory usage beats 38.42 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        head = ListNode(-1,head)
        prev = head
        h1 = head.next
        while h1:
            if h1.val==val:
                prev.next = None
            else:
                prev.next = h1
                prev = prev.next
            h1 = h1.next
        return head.next