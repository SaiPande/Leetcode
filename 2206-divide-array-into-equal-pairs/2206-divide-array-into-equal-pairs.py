class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0)+1

        for key, value in dict1.items():
            if value%2 == 1:
                return False
        return True     