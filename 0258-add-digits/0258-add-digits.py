class Solution:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num
        sum = 0 
        flag = True
        while flag:
            if num == 0 and sum > 9:
                num = sum
                sum = 0
            sum += num%10
            num = num//10
            if sum<=9 and num == 0:
                break
            
        return sum        