class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pless = []
        pmore = []
        pequal = []
        for i in nums:
            if i < pivot:
                pless.append(i)
            elif i > pivot:
                pmore.append(i)
            else:
                pequal.append(i)
        return pless+pequal+pmore              