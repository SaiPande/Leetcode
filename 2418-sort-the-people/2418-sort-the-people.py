class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        '''result = dict(zip(names, heights))
        print(result)
        lst=sorted(result, key = result.get)
        return lst[::-1]'''

        result = list(zip(heights, names))
        lst=sorted(result)
        return [names for heights,names in lst][::-1]

