class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        count = 0
        sign = 1

        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        if (dividend < 0 and divisor >0) or (dividend > 0 and divisor<0):
            sign = -1

        # div = dividend if dividend>0 else -dividend
        # dis = divisor if divisor>0 else -divisor
        div = dividend if dividend < 0 else -dividend  # turning to negating to avoid overflowing
        dis = divisor if divisor < 0 else -divisor


        while div<=dis:
            poweroftwo = -1
            value = dis

            while value >= HALF_MIN_INT and value+value >= div:
                value+=value
                poweroftwo += poweroftwo

            q += poweroftwo
            div -= value

        return -q if sign == 1 else q


        # count = 0
        # sign = 1
            
        # if (dividend < 0 and divisor >0) or (dividend > 0 and divisor<0):
        #     sign = -1
        # div = abs(dividend)
        # dis = abs(divisor)    
        # while div >= dis:
        #     div = div - dis
        #     count += 1

        # if count*sign > 2**31-1:
        #     return 2**31-1
        # elif count*sign < -2**31:
        #     return -2**31
        # else:
        #     return count if sign == 1 else -1*count
  