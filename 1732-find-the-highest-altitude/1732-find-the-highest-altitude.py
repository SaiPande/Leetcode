class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0
        cnt = 0
        for i in gain:
            cnt += i
             
            if cnt> max:
                max = cnt

        return max         