class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0)+1

        maxval = max(dict1.values()) 

        max_elements = [k for k, v in dict1.items() if v == maxval]
        min_distance = 9999999

        for i in max_elements:
            firstocc = nums.index(i)
            lastocc = len(nums) - 1 - nums[::-1].index(i)

            lenth = lastocc-firstocc+1

            if lenth < min_distance:
                min_distance = lenth
   
        return min_distance        