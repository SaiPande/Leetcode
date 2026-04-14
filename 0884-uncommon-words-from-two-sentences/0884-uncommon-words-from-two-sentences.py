class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dict1 = {}
        dict2 = {}

        for i in s1.split():
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        print(dict1)       

        for i in s2.split():
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1  

        output = []

        for key, value in dict1.items():
            if key not in dict2 and value == 1:
                output.append(key)  

        for key, value in dict2.items():
            if key not in dict1 and value == 1:
                output.append(key)            

        print(output)
        return output



