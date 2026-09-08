class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        unique = set()
        duplicate = set()

        for i in nums:
            if i not in unique:
                unique.add(i)
            else:
                duplicate.add(i)

        return list(duplicate)            
