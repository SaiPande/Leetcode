class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num = 0
        for i in range(len(digits)):
            num+=10**(len(digits)-i-1)*digits[i]
        num += 1
        return [int(char) for char in str(num)]

