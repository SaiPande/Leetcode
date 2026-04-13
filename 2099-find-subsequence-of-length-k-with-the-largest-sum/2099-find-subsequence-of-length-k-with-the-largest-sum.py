class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indicesvaluepair = [(nums, i) for i, nums in enumerate(nums)]
        indicesvaluepair.sort(key=lambda x: -x[0])

        top = sorted(indicesvaluepair[:k], key = lambda x: x[1])
        return [i for i,_ in top]
