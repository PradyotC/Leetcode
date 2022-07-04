/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.99 %
    Runtime : 117 ms
    Memory Usage : 14 MB
    Testcase : 1568 / 1568 passed
    Ranking : 
        Your runtime beats 34.25 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2: return 
        if not l1: return l2
        if not l2: return l1
        a1 = ListNode()
        c = 0
        ans = a1
        while l1 and l2:
            a,b = l1.val,l2.val
            a1.next = ListNode((a+b+c)%10)
            c = (a+b+c)//10
            a1 = a1.next
            l1 = l1.next
            l2 = l2.next
        # print(l1,l2,ans.next,a1,c,sep="\n")
        if l1 or l2:
            if not l1:
                rem = l2
            else:
                rem = l1
            while rem:
                a1.next = ListNode((rem.val+c)%10)
                c = (rem.val+c)//10  
                a1 = a1.next
                rem = rem.next
        if c!=0:
            a1.next = ListNode(1)
        return ans.next