# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (high + low)//2
            print(mid)
            if isBadVersion(mid):
                if (mid-1)!= 0 and isBadVersion(mid-1) == False:
                    return mid
                high = mid -1
            else:
                low = mid + 1
        return mid