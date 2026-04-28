class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict1 = {}

        for i in words[0]:
            dict1[i] = dict1.get(i,0)+1


        for i in range(len(words)):
            dict2 = {}
            for j in words[i]:
                dict2[j] = dict2.get(j,0)+1
            common_pairs = {k: min(dict1[k], dict2[k]) for k in dict1.keys() & dict2.keys()}    

            dict1 = common_pairs
        lst = []
        for key, value in dict1.items():
           lst.extend([key] * value)
        return lst