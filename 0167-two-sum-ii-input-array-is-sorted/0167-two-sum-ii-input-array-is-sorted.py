class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            s = numbers[l] + numbers[r]
            
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1] 
        return None
        
        
        # dict1 = {}

        # for i, num in enumerate(numbers,1):
        #     if target - num in dict1:
        #         return [dict1[target - num],i]
        #     dict1[num] = i