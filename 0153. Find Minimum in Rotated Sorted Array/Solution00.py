/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 48.13 %
    Runtime : 65 ms
    Memory Usage : 14.2 MB
    Testcase : 150 / 150 passed
    Ranking : 
        Your runtime beats 43.73 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return nums[self.checkZero(nums,0,len(nums)-1)]
        
    def checkZero(self,arr,l,r):
    # print(arr[l],arr[r])
        if r-l>1:
            mid  = l+((r-l)//2)
            min1 = min(arr[l],arr[r],arr[mid])
            if arr[l]>arr[r]:
                if min1 == arr[mid]:
                    # print(arr[l:mid+1],l,mid)
                    return self.checkZero(arr,l,mid)
                else:
                    # print(arr[mid:r+1],mid,r)
                    return self.checkZero(arr,mid,r)
            else:
                if min1 == arr[mid]:
                    # print(arr[mid:r+1],mid,r)
                    return self.checkZero(arr,mid,r)
                else:
                    # print(arr[l:mid+1],l,mid)
                    return self.checkZero(arr,l,mid)
        else:
            # print(arr[l:r+1],l,r)
            if arr[l]<arr[r]:
                return l
            else:
                return r