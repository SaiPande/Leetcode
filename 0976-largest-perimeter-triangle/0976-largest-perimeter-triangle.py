class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        print(nums)
        for i in range(len(nums)-2):
            if nums[i] < (nums[i+1]+nums[i+2]):
                return nums[i]+nums[i+1]+nums[i+2]
        return 0