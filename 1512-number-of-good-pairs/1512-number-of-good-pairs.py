class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # i = 0 
        # j = 1
        # count = 0 

        # while i< j and j< len(nums):
        #     if nums[i] == nums[j]:
        #         count += 1       
        #     if j == len(nums)-1 and i < len(nums)-2:
        #         i += 1
        #         j = i
        #     j+=1    
        # return count
        count = 0
        freq = {}

        for num in nums:
            if num in freq:
                count += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1

        return count