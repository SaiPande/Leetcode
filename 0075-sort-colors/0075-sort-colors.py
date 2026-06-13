class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #DUTCH NATIONAL FLAG ALGORITHM
        # have 3 pointers for each color
        # left, mid = 0 and right = len(nums)-1
        # and check the mid, if its 0 swap to left, if it right swap with right, else leave it as is

        l= m = 0
        r = len(nums)-1

        while m<=r:
            if nums[m] == 0:
                nums[m], nums[l] = nums[l], nums[m]
                l+=1
                m+=1
            elif nums[m] == 2:
                nums[m], nums[r] = nums[r], nums[m]  
                r-=1
            else:
                m+=1



        # count0red = 0
        # count1white = 0
        # count2blue = 0

        # for i in nums:
        #     if i == 0:
        #         count0red +=1
        #     elif i == 1:
        #         count1white +=1
        #     else:
        #         count2blue +=1  

        # nums[:] = [0]*count0red+[1]*count1white+[2]*count2blue       



        # for i in range(len(nums)):
        #     swapped = False

        #     for j in range(0,len(nums)-i-1):

        #         if nums[j+1] < nums[j]:
        #             nums[j+1], nums[j] = nums[j], nums[j+1]
        #             swapped = True
        #     if swapped == False:
        #         break

