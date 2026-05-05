class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        isnum1 = False
        if len(nums1) <= len(nums2):
            for i in nums1:
                dict1[i] = dict1.get(i,0)+1
                isnum1 = True
        else:
            for i in nums2:
                dict1[i] = dict1.get(i,0)+1


        arr = nums2 if isnum1 == True else nums1 
        outputarr = []

        for i in arr:
            if i in dict1 and dict1[i] != 0:
                dict1[i] -= 1
                outputarr.append(i)

        return outputarr        

        