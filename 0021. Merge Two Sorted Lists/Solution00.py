/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 60.87 %
    Runtime : 79 ms
    Memory Usage : 14 MB
    Testcase : 208 / 208 passed
    Ranking : 
        Your runtime beats 10.66 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return 
        if not list1: return list2
        if not list2: return list1
        a = min(list1.val,list2.val)
        if a==list1.val:
            ans = ListNode(list1.val,None)
            list1 = list1.next
        else:
            ans = ListNode(list2.val,None)
            list2 = list2.next
        a1 = ans
        
        while list1 or list2:
            if not list1:
                ans.next = list2
                return a1
            if not list2:
                ans.next = list1
                return a1
            a = min(list1.val,list2.val)
            if a==list1.val:
                ans.next = ListNode(list1.val,None)
                list1 = list1.next
                ans = ans.next
            else:
                ans.next = ListNode(list2.val,None)
                list2 = list2.next
                ans = ans.next
            # print(a1)
            
            
        
        