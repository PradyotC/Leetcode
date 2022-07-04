/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 38.09 %
    Runtime : 83 ms
    Memory Usage : 14.4 MB
    Testcase : 195 / 195 passed
    Ranking : 
        Your runtime beats 14.73 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val = self.checkZero(nums,0,len(nums)-1)
        nums = nums[val:]+nums[:val]
        v1 = self.binary_search(nums, 0, len(nums)-1, target)
        if v1==-1:
            return -1
        return (v1+val)%len(nums)
        
    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1
    
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