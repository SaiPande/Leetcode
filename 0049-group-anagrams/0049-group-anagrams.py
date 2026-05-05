class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]    
        # outputlst = []
        # dict1 = {}
    
        # opt = []
        # dict2 = {}
        # for i in range(len(strs)):
        #     sortedstr = ''.join(sorted(strs[i]))
        #     opt.append(sortedstr)
        #     dict2[strs[i]] = sortedstr

        # print(dict2)    

        # for key, value in dict2.items():
        #     if not value in dict1:
        #         dict1[value] = [key]
        #     else:
        #         s = ''.join(key)
        #         dict1[value].append(s)    

        # print(dict1)

        # for value in dict1.values():
        #     outputlst.append(value)

        # i = 0
        # while i<len(outputlst)-1:
        #     if outputlst[i] in outputlst[i+1:]:
        #         print(outputlst[i])
        #     i += 1    

        # return outputlst        
            
        dict1 = defaultdict(list)
        
        for i in strs:
            sortedword = ''.join(sorted(i))
            dict1[sortedword].append(i)    

        return list(dict1.values())    