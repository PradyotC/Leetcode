/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 61.19 %
    Runtime : 1117 ms
    Memory Usage : 26.4 MB
    Testcase : 13 / 13 passed
    Ranking : 
        Your runtime beats 33.63 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l1 = len(nums)
        i = 0
        def merge(i,j):
            if j-i==1: return [nums[i]]
            if j-i==2:
                if nums[i]>nums[i+1]: return [nums[i+1],nums[i]]
                return [nums[i],nums[i+1]]
            mid = (j+i)//2
            ret1 = merge(i,mid)
            ret2 = merge(mid,j)
            ans = []
            a,b = 0,0
            while a!=mid-i and b!=j-mid:
                if ret1[a]>ret2[b]:
                    ans.append(ret2[b])
                    b+=1
                else:
                    ans.append(ret1[a])
                    a+=1
                if b==j-mid:
                    ans+=ret1[a:mid-i]
                    break
                if a==mid-i:
                    ans+=ret2[b:j-mid]
                    break
            return ans
        return merge(i,l1)
            
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         l1 = len(nums)
#         i = 0
#         def merge(i,j):
#             if j-i==1: return
#             if j-i==2:
#                 if nums[i]>nums[i+1]: nums.insert(i,nums.pop(i+1))
#                 return
#             mid = (j+i)//2
#             merge(i,mid)
#             merge(mid,j)
#             a,b = i,mid
#             while a!=b and b!=j:
#                 # print(a,b,nums)
#                 if nums[a]>nums[b]:
#                     nums.insert(a,nums.pop(b))
#                     b+=1
#                 a+=1
#             return
#         merge(i,l1)
#         return nums
        