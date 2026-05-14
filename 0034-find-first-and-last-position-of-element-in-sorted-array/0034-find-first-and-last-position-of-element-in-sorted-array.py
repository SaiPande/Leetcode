class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        opt = [-1,-1]
        if len(nums) == 0:
            return opt
        opt[0] = self.binarysearch(nums, target, True)
        opt[1] = self.binarysearch(nums, target, False)
        return opt

    def binarysearch(self, nums: List[int], target: int, findFirst: bool) -> List[int]:
        low = 0
        high = len(nums)-1
        ans = -1

        while low <= high:
            mid = low + (high - low)//2
           
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:    ## nums[mid] == target
                ans = mid
                if findFirst:
                    high = mid-1
                else:
                    low = mid+1
        return ans
    