class Solution:
    def jump(self, nums: List[int]) -> int:
        maxjump = 0
        actualjump = 0
        currentjumpboundary = 0
        for i,jump in enumerate(nums[:-1]):

            if i>maxjump:
                return 0

            maxjump = max(maxjump, i+jump)
           
            if i == currentjumpboundary:
                actualjump += 1
                currentjumpboundary = maxjump           

        return actualjump 