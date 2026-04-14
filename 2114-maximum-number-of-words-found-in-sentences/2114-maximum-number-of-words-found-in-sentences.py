class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_cnt = 0
        for i in sentences:
            cnt = 0
            if '' in i:
                cnt = i.count(' ') + 1
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt        