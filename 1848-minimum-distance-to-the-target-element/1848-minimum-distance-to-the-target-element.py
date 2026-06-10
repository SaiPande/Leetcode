class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        if len(nums)==1:
            return 0
        if start == target:
            return 0
        minval = 99999
        for i in range(len(nums)):
            if nums[i] == target:
                dis = abs(i-start)
                if minval> dis:
                    minval = dis

        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                dis = abs(i-start)
                if minval> dis:
                    minval = dis        
        return minval                