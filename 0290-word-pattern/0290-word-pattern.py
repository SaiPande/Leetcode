class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternlst = list(pattern)
        words = s.split(' ')
        if len(patternlst) != len(words):
            return False
        zip_pattern_ans_s = list(zip(patternlst,words))
        
        dict1 = {}

        for i in range(len(zip_pattern_ans_s)):
            if zip_pattern_ans_s[i][0] in dict1:
                if dict1[zip_pattern_ans_s[i][0]] != zip_pattern_ans_s[i][1]:
                    return False        
            else:
                if zip_pattern_ans_s[i][1] in dict1.values():
                    return False
                dict1[zip_pattern_ans_s[i][0]] = zip_pattern_ans_s[i][1]
        return True        