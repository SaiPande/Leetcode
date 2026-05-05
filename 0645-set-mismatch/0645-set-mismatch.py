class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        length = len(nums)

        correctedsum = (length*(length+1))//2
        numsumlist = sum(nums)
        numsumset = sum(set(nums))

        missing = correctedsum - numsumset
        incorrect = numsumlist - numsumset

        return [incorrect,missing]

        
