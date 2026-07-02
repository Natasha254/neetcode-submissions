class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            count = 0
            return count
        if len(nums) == 1:
            count = 1
            return count
        
        nums = sorted(set(nums))
        current_count = 1
        max_count = 1 
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 1
        return max(max_count, current_count)