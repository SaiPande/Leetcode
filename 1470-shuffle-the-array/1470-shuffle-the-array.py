class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        half = len(nums)//2
        for i in range(half):
            output.append(nums[i])
            output.append(nums[half+i])
        return output    