class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        count = 1
        for i in nums:
            if i-1 not in nums:
                c = 1
                j = i
                while j+1 in nums: 
                    c+=1
                    j+=1
                count = max(count,c)
        return count
        