from typing import List

class Practice88:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while(len(nums1) - m) :
            i = len(nums1) - 1
            if nums1[i] == 0:
                del(nums1[i])
            else :
                break
            i-=1    
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        

if __name__ == "__main__":
    obj = Practice88()
    obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
