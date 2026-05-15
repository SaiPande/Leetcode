class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        maxval = 0
        window = s[0:k]
        for i in range(len(window)):
            if window[i] in 'aeiouAEIOU':
                cnt+=1
        maxval = cnt     
        if cnt == k:
            return maxval
                    
        for i in range(k,len(s)):
            departing = s[i-k]
            window = s[i-k+1 : i+1]
            if s[i] in 'aeiouAEIOU':
                cnt+=1   
            if cnt > 0 and departing in 'aeiouAEIOU':
                cnt-=1
            if cnt > maxval:
                maxval = cnt   
            if maxval == k:
                return maxval

        return maxval            




