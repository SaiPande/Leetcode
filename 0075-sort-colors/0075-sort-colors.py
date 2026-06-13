class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0red = 0
        count1white = 0
        count2blue = 0

        for i in nums:
            if i == 0:
                count0red +=1
            elif i == 1:
                count1white +=1
            else:
                count2blue +=1  

        nums[:] = [0]*count0red+[1]*count1white+[2]*count2blue       



        # for i in range(len(nums)):
        #     swapped = False

        #     for j in range(0,len(nums)-i-1):

        #         if nums[j+1] < nums[j]:
        #             nums[j+1], nums[j] = nums[j], nums[j+1]
        #             swapped = True
        #     if swapped == False:
        #         break

