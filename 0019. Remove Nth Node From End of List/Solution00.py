/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.70 %
    Runtime : 36 ms
    Memory Usage : 13.9 MB
    Testcase : 208 / 208 passed
    Ranking : 
        Your runtime beats 88.84 % of python3 submissions.
        Your memory usage beats 69.42 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode(0,head)
        h1 = head
        c = 0
        while h1:
            h1 = h1.next
            c+=1
        h1 = head
        c-=n+1
        while c!=0:
            h1 = h1.next
            c-=1
        h1.next = h1.next.next
        return head.next