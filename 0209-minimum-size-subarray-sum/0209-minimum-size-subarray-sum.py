class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lst = []
        n = len(nums)
        leastcount = 9999999
        if len(nums) == 0 or (len(nums) == 1 and nums[0]< target):
            return 0
        if nums[0] >= target or max(nums)>=target:
            return 1
        else:    
            count = 1
            start = 0
            prefixSum = [0]*n
            prefixSum[0] = nums[0]
            i = 0
            while i<n:
                prefixSum[i] = prefixSum[i - 1] + nums[i]
                while prefixSum[i] >= target:
                    count = i-start+1
                    if count < leastcount:
                        leastcount = count
                    prefixSum[i] -= nums[start]
                    start += 1 
                i+=1        
        if leastcount == 9999999:
            return 0
        return leastcount    
