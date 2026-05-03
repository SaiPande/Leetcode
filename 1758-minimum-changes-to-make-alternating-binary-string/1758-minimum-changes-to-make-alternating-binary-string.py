class Solution:
    def minOperations(self, s: str) -> int:
        slen = ''
        slen += s[0]
        
        for i in range(1,len(s)):
            if slen[i-1] == '0':
                slen += '1'
            else:
                slen += '0'

        slen2 = ''.join('1' if c == '0' else '0' for c in slen)       

        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if s[i] != slen[i]:
                count1 += 1
            if s[i] != slen2[i]:
                count2 += 1

        return min(count1,count2)            