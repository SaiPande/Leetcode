class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # speed = 1

        # while True:

        #     hour_needed = 0

        #     for i in piles:
        #         hour_needed += math.ceil(i/speed)

        #     if hour_needed <= h:
        #         return speed
        #     else:
        #         speed+=1

        l = 1
        r = max(piles)

        while l < r:
            speed = l+(r-l)//2
            
            hour_needed = 0
            for i in piles:
                hour_needed += math.ceil(i/speed)

            if hour_needed <= h:
                r = speed

            else:
                l = speed+1

        return l
