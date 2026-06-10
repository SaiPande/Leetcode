class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        if len(nums)==1:
            return 0
        if start == target:
            return 0
        minval = 99999
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i] == target:
                dis = abs(i-start)
                if minval> dis:
                    minval = dis
            if nums[j] == target:
                dis = abs(j-start)
                if minval> dis:
                    minval = dis        
            i+=1
            j-=1
        return minval                