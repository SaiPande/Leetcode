class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        finaloutput =[]

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l<r:
                if nums[l]+nums[r]+nums[i] < 0:
                    l+=1
                elif nums[l]+nums[r]+nums[i] > 0:
                    r-=1
                else:
                    finaloutput.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1    
                    l+=1
                    r-=1
        return finaloutput            

        # return [list(t) for t in finaloutput]
        # if len(nums)<3:
        #     return []
        # nums.sort()
        # finaloutput = set()

        # finaloutput = set()
        # for i in range(len(nums)):
        #     seen = set()
        #     for j in range(i+1,len(nums)):
        #         compliment = -(nums[i] + nums[j])

        #         if compliment in seen:
        #             finaloutput.add(tuple([nums[i], nums[j], compliment]))

        #         seen.add(nums[j]) 

        # return [list(t) for t in finaloutput]