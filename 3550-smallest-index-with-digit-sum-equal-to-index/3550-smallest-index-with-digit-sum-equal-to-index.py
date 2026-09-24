class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            sm = 0
            t = nums[i]
            while t>0:
                sm += t%10
                t = t//10

            if i == sm:
                return i
        return -1        