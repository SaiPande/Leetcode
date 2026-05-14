class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k<1:
            return nums
        n = len(nums)   
        k = k%n 

        for _ in range(k):
            last = nums.pop()
            nums.insert(0,last)