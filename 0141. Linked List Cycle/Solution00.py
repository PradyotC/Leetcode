/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 46.24 %
    Runtime : 76 ms
    Memory Usage : 17.5 MB
    Testcase : 21 / 21 passed
    Ranking : 
        Your runtime beats 62.02 % of python3 submissions.
        Your memory usage beats 66.33 % of python3 submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        if not head.next: return False
        h1 = head
        h2 = head.next
        while h2:
            if h1==h2:
                return True
            else:
                if not h2.next: return False
                h2 = h2.next.next
                h1 = h1.next
        return False
            
            
        