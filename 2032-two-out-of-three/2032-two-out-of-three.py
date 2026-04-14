class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set()

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                set1.add(nums1[i])
            elif nums1[i] in nums3:
                set1.add(nums1[i])    

        for i in range(len(nums2)):
            if nums2[i] in nums3:
                set1.add(nums2[i]) 

        return (list(set1))        