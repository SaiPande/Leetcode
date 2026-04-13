class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = (n*(n+1))//2
        divisible =  n//m
        sum_divisible = m*divisible*(divisible+1)//2
        return total_sum - 2*sum_divisible