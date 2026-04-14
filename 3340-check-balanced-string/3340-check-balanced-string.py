class Solution:
    def isBalanced(self, num: str) -> bool:
        sum1 = 0
        sum2 = 0

        for i in range(0, len(num)):
            if i%2 == 0:
                sum1 += int(num[i])
            else:
                sum2 += int(num[i])

        if sum1 == sum2:
            return True
        else:
            return False                