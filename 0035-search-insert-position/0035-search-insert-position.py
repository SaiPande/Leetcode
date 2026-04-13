class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        finish = len(nums) -1
        while start <= finish:
            mid = (finish + start) // 2

            if nums[mid] == target:    
                return mid 
            elif nums[mid] < target:
                start = mid +1 
            else:
                finish = mid -1
        return start  