class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = list(set(nums))
        distinct_nums.sort()
        print(distinct_nums)
        if len(distinct_nums) >= 3: 
            return distinct_nums[len(distinct_nums)-3]
        else:
            return distinct_nums[len(distinct_nums)-1]    
