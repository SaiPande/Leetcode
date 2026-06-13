class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        finaloutput = set()

        finaloutput = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                compliment = -(nums[i] + nums[j])

                if compliment in seen:
                    finaloutput.add(tuple([nums[i], nums[j], compliment]))

                seen.add(nums[j]) 

        return [list(t) for t in finaloutput]