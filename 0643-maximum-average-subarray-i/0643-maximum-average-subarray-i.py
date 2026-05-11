class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        if len(nums)<k:
            return sum(nums)/len(nums)        
        else:
            sm = sum(nums[:k])
            maxavg = sm/k

            for i in range(k,len(nums)):
                sm= sm+nums[i]-nums[i-k]
                if maxavg < sm/k:
                    maxavg = sm/k

            return maxavg        


