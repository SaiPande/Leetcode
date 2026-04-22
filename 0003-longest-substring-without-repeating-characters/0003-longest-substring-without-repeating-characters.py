class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxlen = 0
        count = 0
        seen = set()
        if len(s)<=1:
            return len(s)
        else:
            while j<len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                    if (j - i + 1) > maxlen:
                        maxlen = j - i + 1
                    j += 1
                else: 
                    seen.remove(s[i])
                    i+=1

        return maxlen    