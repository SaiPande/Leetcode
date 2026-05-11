class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        sm = sum(nums[:k])
        maxval = sm
        for i in range(k,len(nums)):
            sm = sm+nums[i]-nums[i-k]
            if maxval < sm:
                maxval = sm

        return maxval/k     

            # no need of calculating avg at everypoint, sum is enough!   


