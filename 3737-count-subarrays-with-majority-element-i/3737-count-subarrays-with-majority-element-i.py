class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # substr = {}
        #substr1 = []
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         substr1.append(nums[i:j+1])
        
        # Based on "Boyer-Moore Majority Voting Algorithm
        majoritycount = 0
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                cnt += 1 if nums[j] == target else -1
                if cnt > 0:
                    majoritycount += 1
                        

        return majoritycount        





