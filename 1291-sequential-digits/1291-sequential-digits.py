class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numbers = "123456789"
        n = 10
        nums = []

        for l in range(len(str(low)), len(str(high))+1):
            for s in range(n-l):
                num = int(numbers[s:s+l])
                if num>=low and num <= high:
                    nums.append(num)
        return nums            