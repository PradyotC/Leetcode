/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 49.05 %
    Runtime : 84 ms
    Memory Usage : 23.9 MB
    Testcase : 12 / 12 passed
    Ranking : 
        Your runtime beats 98.31 % of python3 submissions.
        Your memory usage beats 95.61 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        c = 0
        while temp:
            temp = temp.next
            c+=1
        c = (c+1)//2
        prev = None
        temp = head
        while c:
            prev = temp
            temp = temp.next
            c-=1
        prev.next = None
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        temp = head
        while temp and prev:
            nxt,pnxt = temp.next,prev.next
            temp.next = prev
            prev.next = nxt
            temp,prev = nxt,pnxt
            