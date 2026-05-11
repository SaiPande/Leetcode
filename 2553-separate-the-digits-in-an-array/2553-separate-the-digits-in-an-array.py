class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        st = ''.join(str(x) for x in nums)
        return [int(char) for char in st]