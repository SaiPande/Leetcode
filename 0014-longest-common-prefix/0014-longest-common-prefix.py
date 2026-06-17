class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # matchingstr = []
        # right = 0
        # while right<len(strs[0]): 
        #     matchingstr = strs[0][:right+1]
        #     for i in range(1,len(strs)):
        #         if right >= len(strs[i]) or strs[i][:right+1] != matchingstr:
        #             return strs[0][:right]
        #     right+=1
        # return strs[0]

        if not strs:
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        print(first)
        print(last)
        i=0
        while i<len(first) and i<len(last) and first[i]==last[i]:
            i+=1
        return first[:i]       

