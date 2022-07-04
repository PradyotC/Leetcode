/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 44.98 %
    Runtime : 75 ms
    Memory Usage : 14 MB
    Testcase : 59 / 59 passed
    Ranking : 
        Your runtime beats 13.76 % of python3 submissions.
        Your memory usage beats 5.49 % of python3 submissions.
}
*/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0: return
        i = 0
        while i<m and nums2:
            if nums1[i]>nums2[0]:
                nums1.insert(i,nums2.pop(0))
                nums1.pop()
                m+=1
            i+=1
        while nums2:
            nums1[i]=nums2.pop(0)
            i+=1
                
                
            
        