class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = []
        i = 0
        j = 0

        while i<len(nums1) and j< len(nums2):
            if nums1[i] > nums2[j]:
                lst.append(nums2[j])
                j+=1
            else:
                lst.append(nums1[i])
                i+=1

        if i != (len(nums1)+1):
            lst.extend(nums1[i:])
        if j != (len(nums2)+1):
            lst.extend(nums2[j:])    

        t = len(lst)
        if t%2 == 0:
            return ((lst[(t//2)-1]) + lst[(t//2)])/2
        else:
            return float(lst[(t//2)])    

