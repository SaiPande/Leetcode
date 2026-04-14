class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set1 = set(allowed)
        count = 0
        for i in words:
            set2 = set(i) 
            if set2 <= set1:
                count +=1 
        return count