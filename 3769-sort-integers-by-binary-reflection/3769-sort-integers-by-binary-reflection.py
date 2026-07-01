class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        
        opt = []

        for i in nums:
            binarynum = bin(i)[2:]
            opt.append((i, int(binarynum[::-1],2)))

        opt.sort(key=lambda x: (x[1], x[0]))
        return [i[0] for i in opt]   