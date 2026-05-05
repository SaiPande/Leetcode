class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] in dict1:
                if dict1[s[i]] != t[i]:
                    return False
            else:    
                dict1[s[i]] = t[i]
        
            if t[i] in dict2:
                if dict2[t[i]] != s[i]:
                    return False
            else:    
                dict2[t[i]] = s[i]               
        return True
