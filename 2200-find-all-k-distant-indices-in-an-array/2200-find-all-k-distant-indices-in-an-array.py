class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        print(nums)
        outputlist = []
        for i in range(len(nums)):
            if (nums[i] == key):
                for j in range(len(nums)):
                    if abs(i-j) <= k:
                        outputlist.append(j)
        indexset = set(outputlist)
        return list(indexset)           