class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        output = []
        mini = 999999
        dict1 = {}
        for i in range(len(list1)):
            if list1[i] in list2:
                indexnum2 = list2.index(list1[i])
                if (i+indexnum2) <= mini:
                    mini = i+indexnum2
                    dict1[list1[i]] = mini
        minval = min(dict1.values())
        return [k for k,v in dict1.items() if v == minval]
