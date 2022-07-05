class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        count = 1
        for i in nums:
            if i-1 not in nums:
                c = 0
                while i+c in nums: 
                    c+=1
                count = max(count,c)
        return count
        