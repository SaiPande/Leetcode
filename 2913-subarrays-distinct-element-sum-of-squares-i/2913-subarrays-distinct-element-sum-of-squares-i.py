class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        lst = []
        maxdis = 0
        for i in range(n):
            for j in range(i+1, n+1):
                lst.append(set(nums[i:j]))
    
        for i in lst:
            maxdis += len(i)**2


        return maxdis    