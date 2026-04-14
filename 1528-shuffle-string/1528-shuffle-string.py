class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lst = zip(indices, list(s))        
        
        first, second = zip(*sorted(lst))

        return ''.join(second)
