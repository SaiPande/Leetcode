class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        firsttotal = 0
        for i in range(len(nums)):        
            if (total - firsttotal-nums[i]) == firsttotal:
                return i
            firsttotal += nums[i]    
        return -1            