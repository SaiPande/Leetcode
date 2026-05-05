class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 1
        # for i in range((x//2)+1):
        #     print(i)
        #     if i*i == x:
        #         return i
        #     elif i*i > x: 
        #         return i-1

        if x == 0 or x == 1:
            return x

        low = 1
        high = x

        while low <= high:
            mid =low + (high-low)//2

            if mid*mid == x:
                return mid

            elif mid*mid > x:
                high = mid -1
            else:
                low = mid + 1        
        return high