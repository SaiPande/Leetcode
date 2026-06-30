class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=0
        freq = {'a':-1,'b':-1,'c':-1}
        for i,char in enumerate(s):
            if char in freq:
                freq[char] = i
            min_pos = min(freq['a'], freq['b'], freq['c'])
            if min_pos != -1:
                count += min_pos + 1
        return count        