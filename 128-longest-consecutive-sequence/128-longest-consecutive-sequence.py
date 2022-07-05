class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        for i in nums:
            c = 1
            if i-1 not in nums:
                j = i
                while j+1 in nums: 
                    c+=1
                    j+=1
            count = max(count,c)
        return count
        