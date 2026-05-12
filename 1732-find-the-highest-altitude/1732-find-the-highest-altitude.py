class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = [0]*(len(gain)+1)
        sm = 0
        maxval = 0
        for i in range(len(gain)):
            pre[i+1] = gain[i] + pre[i]
            if pre[i+1]>maxval:
                maxval = pre[i+1]
        return maxval
