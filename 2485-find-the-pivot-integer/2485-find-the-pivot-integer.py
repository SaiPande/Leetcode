class Solution:
    def pivotInteger(self, n: int) -> int:
        if n ==1:
            return 1

        lst = range(1,n+1)

        sum1 = 0
        sum2 = 0
        for i in range(len(lst)):
            sum1 = sum(lst[0:i+1])
            sum2 = sum(lst[i:])


            if sum1 == sum2:
                return i+1
            elif sum1>sum2:
                return -1    