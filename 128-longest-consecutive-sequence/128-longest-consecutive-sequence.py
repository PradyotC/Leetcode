class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        count = 1
        for i in nums:
            if i-1 not in nums:
                j = i
                while j in nums: j+=1
                count = max(count,j-i)
        return count
        