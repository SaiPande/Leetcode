class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1 = {}

        for i, num in enumerate(numbers,1):
            if target - num in dict1:
                return [dict1[target - num],i]
            dict1[num] = i